def find_second_smallest_num(lst):
    if len(lst) < 751 or max(lst) > 246:
        return None
    sub_lst = lst[246:751]
    if len(set(sub_lst)) <= 1:
        return None
    min_val = min(sub_lst)
    sub_lst.remove(min_val)
    if len(sub_lst) == 0:
        return None
    return min(sub_lst)