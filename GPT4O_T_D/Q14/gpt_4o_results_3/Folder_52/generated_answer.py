def find_second_smallest_num(lst):
    if len(lst) < 67:
        return None
    sublist = lst[64:67]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]