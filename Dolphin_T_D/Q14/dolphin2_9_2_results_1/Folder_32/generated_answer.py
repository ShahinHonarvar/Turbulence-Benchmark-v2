def find_second_smallest_num(lst):
    if len(lst) < 36:
        return None
    sub_lst = lst[32:36]
    sub_lst.sort()
    if len(set(sub_lst)) < 2:
        return None
    return sub_lst[1]