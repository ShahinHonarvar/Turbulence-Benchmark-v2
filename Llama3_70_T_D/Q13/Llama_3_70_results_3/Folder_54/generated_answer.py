def find_second_largest_num(lst):
    if len(lst) < 56:
        return None
    sub_lst = lst[34:56]
    sub_lst.sort(reverse=True)
    if len(sub_lst) < 2:
        return None
    return sub_lst[1]