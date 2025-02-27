def all_neg_ints_inclusive(numbers):
    start = 4
    end = 4
    neg_ints = [num for num in numbers[start:end + 1] if num < 0]
    return neg_ints