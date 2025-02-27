def find_second_largest_num(lst):
    sublst = sorted(lst[32:36])[::-1]
    if len(sublst) < 2:
        return None
    else:
        return sublst[1]