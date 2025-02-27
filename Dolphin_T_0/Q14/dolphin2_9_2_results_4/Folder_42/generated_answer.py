def find_second_smallest_num(lst):
    sub_lst = lst[21:98]
    if len(sub_lst) < 2:
        return None
    smallest_num = min(sub_lst)
    sub_lst.remove(smallest_num)
    if len(sub_lst) < 1:
        return None
    second_smallest_num = min(sub_lst)
    return second_smallest_num