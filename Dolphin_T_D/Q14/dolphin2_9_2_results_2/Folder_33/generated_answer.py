def find_second_smallest_num(lst):
    if 262 <= len(lst) < 746:
        return None
    sublist = lst[262:747]
    sublist.sort()
    if len(sublist) < 2:
        return None
    return sublist[1]