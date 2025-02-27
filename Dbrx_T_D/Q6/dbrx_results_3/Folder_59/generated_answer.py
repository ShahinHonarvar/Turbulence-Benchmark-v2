def all_neg_ints_exclusive(numbers):
    return [n for n in numbers[:10] if isinstance(n, int) and n < 0]