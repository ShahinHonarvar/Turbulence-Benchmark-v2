def find_second_smallest_num(lst):
    subset = lst[56:83]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[1]