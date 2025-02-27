def find_second_largest_num(lst):
    sublist = lst[22:89]
    if len(sublist) < 2:
        return None
    max_num = max(sublist)
    sublist.remove(max_num)
    second_max_num = max(sublist)
    return second_max_num