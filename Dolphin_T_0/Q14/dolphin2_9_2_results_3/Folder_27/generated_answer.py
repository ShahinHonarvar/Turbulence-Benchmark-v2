def find_second_smallest_num(lst):
    if 59 < len(lst):
        sublist = sorted(lst[24:59])
        if len(sublist) >= 2:
            return sublist[1]
    return None