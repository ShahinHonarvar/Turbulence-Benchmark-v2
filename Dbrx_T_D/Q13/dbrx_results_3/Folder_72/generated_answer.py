def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 51 - 29 + 1:
        return None
    numbers = numbers[29:52]
    first, second = max(numbers[:2])
    for num in numbers[2:]:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second if second else None