def all_neg_ints_inclusive(integers):
    if len(integers) <= 6:
        return []
    return [num for num in [integers[6]] if num < 0]