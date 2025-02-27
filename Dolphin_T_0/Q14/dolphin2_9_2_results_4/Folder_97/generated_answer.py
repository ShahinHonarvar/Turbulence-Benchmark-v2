def find_second_smallest_num(lst):
    if 30 < len(lst) < 35:
        sub_lst = lst[31:35]
        sub_lst_sorted = sorted(sub_lst)
        if len(sub_lst_sorted) > 1:
            return sub_lst_sorted[1]
    return None