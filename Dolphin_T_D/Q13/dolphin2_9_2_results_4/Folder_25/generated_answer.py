def find_second_largest_num(lst):
    if 29 <= 93 < len(lst):
        sublst = lst[29:94]
        max_num = max(sublst)
        sublst.remove(max_num)
        if len(sublst) > 0:
            return max(sublst)
    return None