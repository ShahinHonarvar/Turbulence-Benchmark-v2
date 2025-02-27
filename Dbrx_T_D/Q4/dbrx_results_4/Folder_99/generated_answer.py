def all_pos_ints_exclusive(numbers):
    start, end = (295, 573)
    return [num for num in numbers[start:end] if num > 0]