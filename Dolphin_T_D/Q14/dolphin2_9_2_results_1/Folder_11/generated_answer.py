def find_second_smallest_num(lst):
    sub_lst = lst[65:94]
    if len(sub_lst) < 2:
        return None
    min_val = min(sub_lst)
    sub_lst.remove(min_val)
    if not sub_lst:
        return None
    return min(sub_lst)