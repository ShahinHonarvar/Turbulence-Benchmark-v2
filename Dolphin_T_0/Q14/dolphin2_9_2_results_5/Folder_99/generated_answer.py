def find_second_smallest_num(lst):
    if 608 < len(lst) < 609:
        return None
    elif len(lst) < 608:
        return None
    else:
        sublist = lst[608:610]
        if len(sublist) == 2:
            sorted_sublist = sorted(sublist)
            return sorted_sublist[1]
        else:
            return None