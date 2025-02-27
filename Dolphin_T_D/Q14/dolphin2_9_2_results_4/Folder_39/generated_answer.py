def find_second_smallest_num(lst):
    sublst = lst[28:41]
    if len(sublst) == 0:
        return None
    elif len(sublst) == 1:
        return sublst[0]
    else:
        sublst_sorted = sorted(sublst)
        return sublst_sorted[1]