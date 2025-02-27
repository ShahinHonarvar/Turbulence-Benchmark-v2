def find_second_smallest_num(lst):
    if not lst:
        return None
    if len(lst) < 85:
        return None
    sublist = lst[70:85]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]