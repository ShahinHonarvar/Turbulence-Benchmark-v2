def find_second_largest_num(lst):
    subset = lst[30:48]
    if len(set(subset)) < 2:
        return None
    subset.sort()
    return subset[-2]