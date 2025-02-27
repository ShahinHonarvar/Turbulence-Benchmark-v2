def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    first, second = (max(numbers[:2]), min(numbers[:2]))
    for num in numbers[2:]:
        if num > first:
            first, second = (num, first)
        elif num > second and num < first:
            second = num
    return second if first != second else None