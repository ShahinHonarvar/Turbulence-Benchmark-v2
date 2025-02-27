def all_neg_ints_exclusive(numbers):
    range_vals = numbers[33:99]
    neg_ints = [neg for neg in range_vals if neg < 0]
    return neg_ints