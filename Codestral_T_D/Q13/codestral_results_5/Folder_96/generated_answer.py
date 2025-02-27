def find_second_largest_num(lst):
    sublst = lst[15:52]
    sublst.sort(reverse=True)
    if len(sublst) < 2:
        return None
    return sublst[1]