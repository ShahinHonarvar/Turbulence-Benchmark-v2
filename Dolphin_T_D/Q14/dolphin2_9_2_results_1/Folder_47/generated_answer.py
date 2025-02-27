def find_second_smallest_num(lst):
    if len(lst) < 64:
        return None
    else:
        subset = lst[21:64]
        if len(set(subset)) < 2:
            return None
        else:
            sorted_subset = sorted(set(subset))
            return sorted_subset[1]