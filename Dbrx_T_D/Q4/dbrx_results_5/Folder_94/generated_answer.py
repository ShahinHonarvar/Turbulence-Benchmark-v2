def all_pos_ints_exclusive(numbers):
    start, end = (28, 53)
    return [n for n in numbers[start:end] if 0 < n < end - start]