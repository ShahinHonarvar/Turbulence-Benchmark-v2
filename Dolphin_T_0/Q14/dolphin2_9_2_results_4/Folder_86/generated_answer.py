def find_second_smallest_num(lst):
    if 36 < len(lst) < 33:
        subset = lst[33:37]
        if len(subset) < 2:
            return None
        subset.sort()
        return subset[1]
    else:
        return None