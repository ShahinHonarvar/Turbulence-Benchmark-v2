def find_second_largest_num(lst):
    if len(lst) <= 23:
        return None
    sublist = lst[23:24]
    if len(sublist) < 2:
        return None
    return sorted(sublist)[-2]