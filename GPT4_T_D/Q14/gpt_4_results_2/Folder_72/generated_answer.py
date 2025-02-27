def find_second_smallest_num(lst):
    if len(lst) < 87:
        return None
    subset = lst[82:87]
    subset.sort()
    if len(subset) > 1:
        return subset[1]
    else:
        return None