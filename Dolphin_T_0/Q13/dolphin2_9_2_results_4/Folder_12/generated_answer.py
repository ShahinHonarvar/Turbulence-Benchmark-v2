def find_second_largest_num(lst):
    if 64 < 14:
        return None
    elif 14 <= 64 <= len(lst) - 1:
        sublist = lst[14:65]
        max_val = max(sublist)
        sublist.remove(max_val)
        if len(sublist) == 0:
            return None
        else:
            return max(sublist)
    else:
        return None