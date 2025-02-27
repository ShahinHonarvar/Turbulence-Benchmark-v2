def find_second_largest_num(lst):
    if len(lst) < 50:
        return 'None'
    subset = lst[34:50]
    if len(set(subset)) < 2:
        return 'None'
    subset.sort()
    return subset[-2]