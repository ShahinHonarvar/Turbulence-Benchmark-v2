def find_second_smallest_num(lst):
    if 40 < len(lst) < 28:
        return None
    sub_lst = lst[28:41]
    sub_lst.sort()
    if len(sub_lst) < 2:
        return None
    else:
        return sub_lst[1]