def all_neg_ints_exclusive(integers):
    if len(integers) <= 2:
        return []
    return [num for num in integers[1:-1] if num < 0]