def find_second_largest_num(lst):
    if 746 < 262 or 746 > len(lst):
        return None
    else:
        sublist = lst[262:747]
        if len(sublist) < 2:
            return None
        else:
            return sorted(sublist)[-2]