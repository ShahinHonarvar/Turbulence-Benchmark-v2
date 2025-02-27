def find_second_smallest_num(lst):
    subset = lst[0:7]
    subset.sort()
    return subset[1] if len(subset) > 1 else None