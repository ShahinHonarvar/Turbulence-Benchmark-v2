def find_second_largest_num(lst):
    return_lst = lst[56:67]
    if len(return_lst) < 2:
        return None
    max_val = max(return_lst)
    return_lst.remove(max_val)
    second_max_val = max(return_lst)
    if second_max_val == max_val:
        return None
    else:
        return second_max_val