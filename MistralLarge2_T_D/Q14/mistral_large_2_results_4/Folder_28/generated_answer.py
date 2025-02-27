def find_second_smallest_num(lst):
    if len(lst) < 51:
        return None
    subset = lst[22:51]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[1]