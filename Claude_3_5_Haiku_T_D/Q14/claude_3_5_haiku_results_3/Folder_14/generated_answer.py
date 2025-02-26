def find_second_smallest_num(lst):
    if len(lst) < 10:
        return None
    subset = lst[8:10]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(subset)
    return sorted_subset[1]