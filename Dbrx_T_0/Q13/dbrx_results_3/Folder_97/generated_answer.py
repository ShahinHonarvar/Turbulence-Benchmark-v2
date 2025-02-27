def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 41 or len(numbers) > 81:
        return None
    first, second = (max(numbers[40:81]), None)
    for num in numbers[40:81]:
        if num > first:
            first, second = (num, first)
        elif num != first and (second is None or num > second):
            second = num
    return second