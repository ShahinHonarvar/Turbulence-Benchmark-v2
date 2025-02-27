def find_second_largest_num(lst):
    if 56 <= 66 < len(lst):
        sub_lst = sorted(lst[56:67])
        return sub_lst[-2] if len(sub_lst) > 1 else None
    else:
        return None