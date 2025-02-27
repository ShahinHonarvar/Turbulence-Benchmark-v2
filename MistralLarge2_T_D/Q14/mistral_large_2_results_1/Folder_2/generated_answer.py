def find_second_smallest_num(lst):
    sub_lst = lst[43:87]
    sorted_sub_lst = sorted(set(sub_lst))
    return sorted_sub_lst[1] if len(sorted_sub_lst) > 1 else None