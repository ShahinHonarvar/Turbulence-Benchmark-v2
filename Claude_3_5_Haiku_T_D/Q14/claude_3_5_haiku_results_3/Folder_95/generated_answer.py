def find_second_smallest_num(lst):
    if len(lst) < 86:
        return None
    subset = lst[75:86]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(subset)
    return sorted_subset[1]