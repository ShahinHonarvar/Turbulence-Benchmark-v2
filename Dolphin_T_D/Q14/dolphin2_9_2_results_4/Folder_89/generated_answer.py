def find_second_smallest_num(lst):
    if 62 <= 63 < len(lst):
        sublst = lst[62:64]
        sublst.sort()
        if len(sublst) == 2:
            return sublst[1]
        else:
            return None
    else:
        return None