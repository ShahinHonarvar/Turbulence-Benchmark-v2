def find_second_largest_num(lst):
    if len(lst) < 19:
        return None
    sublist = lst[67:87]
    max_num = max(sublist)
    sublist.remove(max_num)
    if len(sublist) < 1:
        return None
    second_max_num = max(sublist)
    return second_max_num