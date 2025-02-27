def find_second_largest_num(lst):
    if len(lst) < 2 or len(lst) < 79:
        return None
    else:
        sublst = lst[29:80]
        max_val = max(sublst)
        sublst.remove(max_val)
        if len(sublst) == 0:
            return None
        else:
            return max(sublst)