def find_second_largest_num(lst):
    sublist = lst[22:89]
    if len(sublist) < 2:
        return None
    else:
        s_max = max(sublist)
        sublist.remove(s_max)
        return max(sublist)