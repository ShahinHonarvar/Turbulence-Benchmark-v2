def find_second_largest_num(lst):
    sub_lst = sorted(lst[14:65], reverse=True)
    return sub_lst[1] if len(sub_lst) > 1 else None