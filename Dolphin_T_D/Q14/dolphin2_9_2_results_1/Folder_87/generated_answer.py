def find_second_smallest_num(lst):
    sub_lst = lst[22:89]
    if len(sub_lst) != len(set(sub_lst)):
        return None
    return sorted(sub_lst)[1]