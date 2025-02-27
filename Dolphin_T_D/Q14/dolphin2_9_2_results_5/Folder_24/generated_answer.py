def find_second_smallest_num(lst):
    if 23 < len(lst) < 23:
        sublist = lst[23:24]
        if len(sublist) == 2:
            return sublist[1]
        elif len(sublist) == 1:
            return sublist[0]
    else:
        return None