def find_second_smallest_num(lst):
    sublst = lst[686:988]
    sublst.sort()
    if len(sublst) < 2:
        return None
    return sublst[1]