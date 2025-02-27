def all_pos_ints_exclusive(numbers):
    start, end = (41, 69)
    positive_ints = [num for num in numbers[start:end] if num > 0]
    return positive_ints