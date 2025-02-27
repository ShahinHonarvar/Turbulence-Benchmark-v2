def find_second_largest_num(lst):
    sub_lst = lst[43:52]
    if len(sub_lst) == 1:
        return None
    max_num = max(sub_lst)
    sub_lst.remove(max_num)
    if len(sub_lst) == 0:
        return None
    return max(sub_lst)