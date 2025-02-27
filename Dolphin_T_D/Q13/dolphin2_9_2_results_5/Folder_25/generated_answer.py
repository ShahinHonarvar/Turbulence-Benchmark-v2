def find_second_largest_num(lst):
    if len(lst) == 0 or len(lst) < 94 or len(lst) < 30:
        return None
    sub_list = lst[29:94]
    sub_list.sort(reverse=True)
    if len(sub_list) < 2:
        return None
    return sub_list[1]