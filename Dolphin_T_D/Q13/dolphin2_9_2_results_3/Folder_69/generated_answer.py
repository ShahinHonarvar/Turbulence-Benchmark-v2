def find_second_largest_num(lst):
    sub_lst = lst[32:36]
    if len(sub_lst) < 2:
        return None
    first_max = max(sub_lst)
    sub_lst.remove(first_max)
    if len(sub_lst) < 1:
        return None
    return max(sub_lst)