def find_second_smallest_num(lst):
    sublist = lst[10:11] if 10 < len(lst) else []
    if len(sublist) < 2:
        return None
    sublist.sort()
    sublist.pop(0)
    if len(sublist) < 1:
        return None
    return sublist[0]