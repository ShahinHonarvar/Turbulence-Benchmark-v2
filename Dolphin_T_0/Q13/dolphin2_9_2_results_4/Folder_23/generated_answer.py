def find_second_largest_num(lst):
    if 71 >= len(lst) or 52 < 0:
        return None
    sublst = lst[52:72]
    if len(sublst) < 2:
        return None
    sublst.sort()
    return sublst[-2]