def find_second_largest_num(lst):
    if 93 >= len(lst) or 29 < 0:
        return None
    subset = sorted(lst[29:94], reverse=True)
    if len(subset) < 2:
        return None
    return subset[1]