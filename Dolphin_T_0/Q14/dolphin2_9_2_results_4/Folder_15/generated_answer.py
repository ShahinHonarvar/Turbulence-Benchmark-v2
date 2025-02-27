def find_second_smallest_num(lst):
    if len(lst) < 4:
        return None
    subset = lst[:4]
    subset.sort()
    if len(subset) < 2:
        return None
    return subset[1]