def all_pos_ints_exclusive(numbers):
    start, end = (70, 98)
    result = [num for num in numbers[start:end] if num > 0]
    return result