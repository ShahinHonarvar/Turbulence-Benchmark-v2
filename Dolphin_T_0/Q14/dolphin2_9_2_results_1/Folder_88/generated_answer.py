def find_second_smallest_num(lst):
    sublst = lst[5:9]
    if len(sublst) < 2:
        return None
    sublst.sort()
    return sublst[1]