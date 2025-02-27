def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) - 1 < 23:
        return None
    first, second = (max(numbers[:24]), None)
    for num in numbers[24:]:
        if num > first:
            first, second = (num, first)
        elif num > second and num < first:
            second = num
    return second