def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 30 or len(numbers) < 200:
        return None
    first, second = (max(numbers[30:200]), None)
    for num in numbers[30:200]:
        if num > first:
            first, second = (num, first)
        elif second is None or num > second:
            second = num
    return second