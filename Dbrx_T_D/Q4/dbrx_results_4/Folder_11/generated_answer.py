def all_pos_ints_exclusive(numbers):
    start, end = (15, 99)
    return [n for n in numbers[start:end] if n > 0]