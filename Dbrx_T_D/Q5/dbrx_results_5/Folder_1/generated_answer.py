def all_neg_ints_inclusive(numbers):
    start = 31
    end = 72
    return [num for num in numbers[start:end + 1] if num < 0]