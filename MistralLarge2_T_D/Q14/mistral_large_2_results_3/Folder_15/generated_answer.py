def find_second_smallest_num(lst):
    if len(lst) < 2:
        return None
    sublist = lst[:4]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]