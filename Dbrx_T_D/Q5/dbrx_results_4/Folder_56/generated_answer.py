def all_neg_ints_inclusive(numbers):
    return [num for num in numbers[:1] if num < 0] + [num for num in numbers[1:] if num < 0]