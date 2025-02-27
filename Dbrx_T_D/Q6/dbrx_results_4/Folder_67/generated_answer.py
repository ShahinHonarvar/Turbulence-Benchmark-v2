def all_neg_ints_exclusive(numbers):
    start, end = (49, 74)
    return [num for num in numbers[start:end] if num < 0]