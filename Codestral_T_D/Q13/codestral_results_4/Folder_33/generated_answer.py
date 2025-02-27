def find_second_largest_num(lst):
    sub_lst = sorted(lst[667:775])
    if len(sub_lst) >= 2:
        return sub_lst[-2]
    return None