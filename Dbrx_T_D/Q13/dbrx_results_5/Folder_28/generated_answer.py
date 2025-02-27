def find_second_largest_num(numbers):
    numbers_subset = numbers[62:64]
    if len(numbers_subset) < 2:
        return None
    first, second = (max(numbers_subset), max(numbers_subset[:-1] + numbers_subset[1:]))
    return second if first != second else None