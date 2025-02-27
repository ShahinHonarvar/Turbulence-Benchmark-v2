def find_second_smallest_num(lst):
    sub_lst = lst[59:98]
    if len(sub_lst) < 2:
        return None
    return sorted(sub_lst)[1]