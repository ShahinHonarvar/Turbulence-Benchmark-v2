def find_second_smallest_num(lst):
    sub_lst = lst[22:64]
    if len(sub_lst) < 2:
        return None
    else:
        sorted_sub_lst = sorted(sub_lst)
        return sorted_sub_lst[1]