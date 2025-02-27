def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 775 or index not in range(len(numbers)):
        return None
    first, second = (max(numbers[667:775]), None)
    for num in numbers[667:775]:
        if num > first:
            first, second = (num, first)
        elif num != first and (second is None or num > second):
            second = num
    return second