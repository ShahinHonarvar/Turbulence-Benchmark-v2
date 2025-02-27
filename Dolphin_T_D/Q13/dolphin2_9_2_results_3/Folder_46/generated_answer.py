def find_second_largest_num(lst):
    if 87 < len(lst) < 30:
        return None
    sublist = lst[30:88]
    if len(sublist) < 2:
        return None
    max_num = max(sublist)
    sublist.remove(max_num)
    second_max = max(sublist)
    return second_max