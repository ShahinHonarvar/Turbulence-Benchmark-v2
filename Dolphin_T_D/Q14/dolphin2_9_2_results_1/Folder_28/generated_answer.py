def find_second_smallest_num(lst):
    if not 22 <= 50 < len(lst):
        return None
    sub_lst = lst[22:51]
    if len(set(sub_lst)) != len(sub_lst):
        return None
    sub_lst.sort()
    return sub_lst[1]