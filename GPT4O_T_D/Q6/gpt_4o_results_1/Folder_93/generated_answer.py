def all_neg_ints_exclusive(integers):
    if len(integers) <= 20:
        return []
    return [num for num in integers[20:94] if num < 0]