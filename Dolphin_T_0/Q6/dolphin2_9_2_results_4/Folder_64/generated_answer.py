def all_neg_ints_exclusive(numbers):
    result = [x for x in numbers[1:-1] if x < 0]
    return result