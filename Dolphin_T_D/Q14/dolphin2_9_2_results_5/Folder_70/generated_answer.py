def find_second_smallest_num(lst):
    if 35 <= 49 < len(lst):
        sublst = sorted(lst[35:50])
        if len(sublst) > 2:
            return sublst[1]
    return None