def find_second_smallest_num(lst):
    if lst is None or len(lst) <= 10:
        return None
    sublist = lst[10:11]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1] if len(sublist) > 1 else None