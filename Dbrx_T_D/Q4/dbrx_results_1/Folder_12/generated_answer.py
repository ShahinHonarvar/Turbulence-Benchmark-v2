def all_pos_ints_exclusive(numbers):
    start, end = (23, 45)
    return [num for num in numbers[start:end] if num > 0]