def find_second_smallest_num(lst):
    if len(lst) < 89:
        return None
    subset = sorted(lst[75:89])
    if len(subset) < 2:
        return None
    return subset[1]