def find_second_smallest_num(lst):
    if len(lst) < 40:
        return None
    sublist = lst[15:40]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]