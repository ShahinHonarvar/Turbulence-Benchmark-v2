def find_second_smallest_num(lst):
    if len(lst) < 2 or len(lst) < 87:
        return None
    subset = lst[25:88]
    subset.sort()
    if len(set(subset)) < 2:
        return None
    return subset[1]