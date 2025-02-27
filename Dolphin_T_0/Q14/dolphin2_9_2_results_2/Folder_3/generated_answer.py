def find_second_smallest_num(lst):
    if len(lst) < 56:
        return None
    sublist = lst[27:56]
    if len(sublist) < 2:
        return None
    min1 = min(sublist)
    sublist.remove(min1)
    if len(sublist) < 2:
        return None
    return min(sublist)