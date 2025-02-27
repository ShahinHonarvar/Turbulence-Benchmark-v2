def find_largest_num(lst):
    if len(lst) < 101:
        return None
    return max(lst[10:101])