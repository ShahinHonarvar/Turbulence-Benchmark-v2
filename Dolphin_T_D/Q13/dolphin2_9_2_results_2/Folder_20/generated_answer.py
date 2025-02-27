def find_second_largest_num(lst):
    if len(lst) == 0 or len(lst) < 67:
        return None
    sublist = lst[56:67]
    max_num = max(sublist)
    sublist.remove(max_num)
    if len(sublist) == 0:
        return None
    second_max_num = max(sublist)
    return second_max_num