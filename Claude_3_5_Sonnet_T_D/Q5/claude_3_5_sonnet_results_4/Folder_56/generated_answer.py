def all_neg_ints_inclusive(integers):
    if integers and integers[0] < 0:
        return [integers[0]]
    return []