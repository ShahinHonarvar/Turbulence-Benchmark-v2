def find_second_smallest_num(lst):
    sublst = lst[29:94]
    if len(sublst) < 2:
        return None
    else:
        sublst.sort()
        return sublst[1]