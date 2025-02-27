def find_second_smallest_num(lst):
    sublist = lst[20:31]
    if len(sublist) < 2:
        return None
    min1 = min(sublist)
    sublist.remove(min1)
    if len(sublist) < 2:
        return None
    min2 = min(sublist)
    return min2