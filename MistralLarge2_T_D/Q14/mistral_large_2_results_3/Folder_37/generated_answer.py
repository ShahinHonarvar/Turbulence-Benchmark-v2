def find_second_smallest_num(lst):
    if len(lst) < 8:
        return None
    sublist = lst[5:8]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]