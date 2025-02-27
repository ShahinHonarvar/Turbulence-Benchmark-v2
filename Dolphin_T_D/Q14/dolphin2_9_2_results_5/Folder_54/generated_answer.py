def find_second_smallest_num(lst):
    if len(lst) == 0 or 86 >= len(lst) or 68 < 0:
        return None
    else:
        sublst = lst[68:87]
        mins = sorted(sublst)
        if len(mins) < 2:
            return None
        else:
            return mins[1]