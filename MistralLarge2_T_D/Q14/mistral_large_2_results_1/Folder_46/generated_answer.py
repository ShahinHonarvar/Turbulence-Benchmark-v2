def find_second_smallest_num(lst):
    if len(lst) < 69:
        return None
    sublist = lst[13:69]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]