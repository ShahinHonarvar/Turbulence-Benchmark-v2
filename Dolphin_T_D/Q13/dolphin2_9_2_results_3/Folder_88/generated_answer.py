def find_second_largest_num(lst):
    if len(lst) == 0 or len(lst) < 5:
        return None
    sublist = lst[4:9]
    if len(sublist) < 5:
        return None
    max_num = max(sublist)
    sublist.remove(max_num)
    if len(sublist) == 0:
        return None
    second_max_num = max(sublist)
    return second_max_num