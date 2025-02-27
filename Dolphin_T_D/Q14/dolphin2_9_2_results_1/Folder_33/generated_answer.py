def find_second_smallest_num(lst):
    if not 262 <= 746 < len(lst):
        return None
    subset = lst[262:747]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[1]