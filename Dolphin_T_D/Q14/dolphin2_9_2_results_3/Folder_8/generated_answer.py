def find_second_smallest_num(lst):
    if len(lst) < 2:
        return None
    if len(lst) <= 11:
        return None
    sublist = lst[56:67]
    sublist.sort()
    return sublist[1] if len(sublist) >= 2 else None