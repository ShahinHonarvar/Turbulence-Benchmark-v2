def find_second_smallest_num(lst):
    if len(lst) < 87:
        return None
    subset = sorted(lst[68:87])
    if len(subset) < 2:
        return None
    return subset[1]