def find_second_smallest_num(lst):
    if len(lst) < 750:
        return None
    sublist = lst[246:751]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]