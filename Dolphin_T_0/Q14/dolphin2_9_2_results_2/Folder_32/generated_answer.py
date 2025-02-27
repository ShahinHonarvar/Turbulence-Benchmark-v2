def find_second_smallest_num(lst):
    if len(lst) < 36:
        return None
    sub_lst = lst[31:36]
    sub_lst_sorted = sorted(sub_lst)
    if len(sub_lst_sorted) < 2:
        return None
    else:
        return sub_lst_sorted[1]