def find_second_largest_num(lst):
    if len(lst) < 52:
        return None
    sublist = lst[29:52]
    max_val = max(sublist)
    sublist.remove(max_val)
    if not sublist:
        return None
    second_max_val = max(sublist)
    return second_max_val