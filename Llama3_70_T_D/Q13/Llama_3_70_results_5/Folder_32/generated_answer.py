def find_second_largest_num(lst):
    if len(lst) < 98:
        return None
    sublist = lst[21:98]
    if len(sublist) < 2:
        return None
    return sorted(set(sublist), reverse=True)[1]