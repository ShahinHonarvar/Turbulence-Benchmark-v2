def all_neg_ints_inclusive(numbers):
    return [num for i, num in enumerate(numbers) if -3 <= i <= 2 and num < 0]