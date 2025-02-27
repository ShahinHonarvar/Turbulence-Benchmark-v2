def find_second_largest_num(lst):
    sub_lst = lst[74:96]
    if len(sub_lst) == 0 or len(sub_lst) == 1:
        return None
    max_val = max(sub_lst)
    sub_lst.remove(max_val)
    if len(sub_lst) == 0:
        return None
    second_max_val = max(sub_lst)
    return second_max_val