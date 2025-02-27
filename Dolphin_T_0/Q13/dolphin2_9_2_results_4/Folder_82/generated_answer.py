def find_second_largest_num(lst):
    sublist = lst[20:201]
    if len(sublist) < 2:
        return None
    max_num = max(sublist)
    sublist.remove(max_num)
    if len(sublist) < 2:
        return None
    second_max_num = max(sublist)
    return second_max_num