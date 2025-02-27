def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) - 1 < 23:
        return None
    first, second = max((name for name in numbers[23:23 + 2]))
    for num in numbers[23:]:
        if num > first:
            first, second = (num, first)
        elif num > second and num < first:
            second = num
    return second