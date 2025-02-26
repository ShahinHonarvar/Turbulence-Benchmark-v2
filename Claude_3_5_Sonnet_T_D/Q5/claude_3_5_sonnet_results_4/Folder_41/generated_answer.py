def all_neg_ints_inclusive(integers):
    if len(integers) >= 7:
        if integers[6] < 0:
            return [integers[6]]
    return []