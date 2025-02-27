def all_pos_ints_exclusive(numbers):
    start, end = (20, 93)
    return [n for n in numbers[start - 1:end] if n > 0]