def find_second_smallest_num(lst):
    if 32 < len(lst) < 28:
        return None
    sublist = lst[28:33]
    sublist.sort()
    if len(sublist) < 2:
        return None
    else:
        return sublist[1]