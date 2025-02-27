def find_second_smallest_num(lst):
    if len(lst) < 2:
        return None
    elif len(lst) == 2:
        return None if lst[0] == lst[1] else lst[0]
    sublist = lst[8:10]
    sublist.sort()
    return sublist[1] if len(sublist) == 2 else None