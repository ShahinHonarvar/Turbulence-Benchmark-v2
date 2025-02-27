def find_second_smallest_num(lst):
    if len(lst) < 5:
        return None
    sub_lst = lst[3:6]
    if len(set(sub_lst)) < 2:
        return None
    return sorted(sub_lst)[1]