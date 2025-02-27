def find_second_smallest_num(lst):
    if len(lst) < 36:
        return None
    sublist = lst[33:37]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]