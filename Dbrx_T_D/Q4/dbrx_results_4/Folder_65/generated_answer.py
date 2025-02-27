def all_pos_ints_exclusive(numbers):
    start, end = (42, 87)
    return [n for n in numbers[start:end] if 0 < n]