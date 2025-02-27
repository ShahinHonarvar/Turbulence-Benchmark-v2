def find_second_smallest_num(lst):
    if len(lst) < 59:
        return None
    sub_lst = sorted(lst[25:60])
    if len(sub_lst) < 2:
        return None
    return sub_lst[1]