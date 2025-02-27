def find_second_largest_num(lst):
    if 59 < len(lst) < 25:
        return None
    sub_lst = lst[25:60]
    if len(sub_lst) < 2:
        return None
    first_max = max(sub_lst)
    sub_lst.remove(first_max)
    second_max = max(sub_lst)
    return second_max