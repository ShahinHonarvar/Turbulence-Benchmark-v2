def find_second_smallest_num(lst):
    if not lst or len(lst) < 976:
        return None
    subset = lst[639:976]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(subset)
    return sorted_subset[1]