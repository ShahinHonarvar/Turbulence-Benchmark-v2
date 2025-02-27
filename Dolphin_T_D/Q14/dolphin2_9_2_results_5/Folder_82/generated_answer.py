def find_second_smallest_num(lst):
    if len(lst) < 20:
        return None
    sublist = lst[20:200]
    if len(sublist) == 0:
        return None
    min_num = min(sublist)
    sublist.remove(min_num)
    if len(sublist) == 0:
        return None
    return min(sublist)