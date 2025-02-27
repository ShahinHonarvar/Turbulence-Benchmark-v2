def find_second_largest_num(lst):
    sub_lst = lst[35:50]
    if len(sub_lst) < 2:
        return None
    else:
        max_val = max(sub_lst)
        sub_lst.remove(max_val)
        second_max = max(sub_lst)
        return second_max