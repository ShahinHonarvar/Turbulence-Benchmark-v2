def all_neg_ints_inclusive(numbers):
    start, end = (20, 200)
    return [n for n in numbers[start:end + 1] if n < 0]