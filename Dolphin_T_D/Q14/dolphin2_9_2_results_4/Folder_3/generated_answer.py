def find_second_smallest_num(lst):
    sub_lst = lst[27:56]
    if len(sub_lst) < 2:
        return None
    sub_lst_sorted = sorted(sub_lst)
    return sub_lst_sorted[1]