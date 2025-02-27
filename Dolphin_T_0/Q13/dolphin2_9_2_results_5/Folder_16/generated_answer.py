def find_second_largest_num(lst):
    sub_lst = lst[33:37]
    if len(sub_lst) < 2:
        return None
    max_num = max(sub_lst)
    sub_lst.remove(max_num)
    second_max_num = max(sub_lst)
    return second_max_num