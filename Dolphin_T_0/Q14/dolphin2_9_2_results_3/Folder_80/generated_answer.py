def find_second_smallest_num(lst):
    if 87 < len(lst) < 30:
        return None
    sublist = sorted(lst[30:88])
    if len(sublist) < 2:
        return None
    return sublist[1]