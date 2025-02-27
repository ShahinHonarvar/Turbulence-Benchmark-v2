def find_second_smallest_num(lst):
    subset = lst[75:95]
    if len(subset) < 2:
        return None
    else:
        subset.sort()
        return subset[1]