def find_second_smallest_num(lst):
    if len(lst) < 2:
        return None
    sublist = lst[29:94]
    sublist_set = set(sublist)
    if len(sublist_set) < 2:
        return None
    min_value = min(sublist)
    sublist.remove(min_value)
    if len(sublist) == 0:
        return None
    return min(sublist)