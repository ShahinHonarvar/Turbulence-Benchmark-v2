def find_second_smallest_num(lst):
    sublist = lst[12:93]
    if len(sublist) < 2:
        return None
    min_num = min(sublist)
    sublist.remove(min_num)
    if sublist:
        return min(sublist)
    else:
        return None