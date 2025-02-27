def find_second_smallest_num(lst):
    if len(lst) <= 51:
        return None
    sublist = sorted(lst[37:52])
    if len(sublist) >= 2:
        return sublist[1]
    return None