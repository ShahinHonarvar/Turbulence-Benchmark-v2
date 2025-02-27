def find_second_largest_num(lst):
    if len(lst) == 0 or len(lst) < 92:
        return None
    sublist = lst[19:93]
    if len(sublist) < 2:
        return None
    max_num = max(sublist)
    sublist.remove(max_num)
    second_max = max(sublist)
    return second_max