def find_second_smallest_num(lst):
    sub_lst = lst[21:98]
    if len(sub_lst) < 2:
        return None
    sorted_sub_lst = sorted(sub_lst)
    return sorted_sub_lst[1] if len(sorted_sub_lst) > 1 else None