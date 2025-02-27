def find_second_smallest_num(lst):
    if len(lst) < 64:
        return None
    sublist = sorted(lst[22:64])
    if len(sublist) < 2:
        return None
    return sublist[1]