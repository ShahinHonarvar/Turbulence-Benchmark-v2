def all_pos_ints_exclusive(numbers):
    start, end = (57, 84)
    return [num for num in numbers[start:end] if 0 < num]