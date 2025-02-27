def find_second_largest_num(numbers):
    numbers_subset = numbers[40:201]
    if len(numbers_subset) < 2:
        return None
    first, second = (max(numbers_subset[0], numbers_subset[1]), min(numbers_subset[0], numbers_subset[1]))
    for num in numbers_subset[2:]:
        if num > first:
            first, second = (num, first)
        elif num > second and num != first:
            second = num
    return second