def all_pos_ints_exclusive(numbers):
    range_start = 36
    range_end = 53
    return [num for num in numbers[range_start:range_end] if num > 0]