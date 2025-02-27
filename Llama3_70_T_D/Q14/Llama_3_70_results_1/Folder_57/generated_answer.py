def find_second_smallest_num(lst):
    if len(lst) < 31:
        return None
    else:
        sublist = sorted(lst[20:31])
        if len(sublist) < 2:
            return None
        else:
            return sublist[1]