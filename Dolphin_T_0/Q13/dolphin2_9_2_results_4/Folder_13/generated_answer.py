def find_second_largest_num(lst):
    sublist = lst[25:87]
    if len(sublist) < 2:
        return None
    max_num = max(sublist)
    sublist.remove(max_num)
    if not sublist:
        return None
    second_max = max(sublist)
    return second_max