def find_second_smallest_num(lst):
    if len(lst) < 96:
        return None
    sub_lst = lst[74:96]
    if len(set(sub_lst)) < 2:
        return None
    min1 = min(sub_lst)
    sub_lst.remove(min1)
    if not sub_lst:
        return None
    return min(sub_lst)