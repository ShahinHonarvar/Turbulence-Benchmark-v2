def find_second_smallest_num(lst):
    if 28 < len(lst) < 33:
        sublist = lst[28:33]
    else:
        return None
    sublist.sort()
    if len(sublist) < 2:
        return None
    else:
        return sublist[1]