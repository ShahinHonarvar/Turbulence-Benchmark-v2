def find_second_largest_num(lst):
    subset = lst[32:36]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[-2]