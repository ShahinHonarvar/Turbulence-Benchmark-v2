def all_pos_ints_inclusive(numbers):
    start, end = (19, 92)
    return [num for num in numbers[start:end + 1] if num > 0]