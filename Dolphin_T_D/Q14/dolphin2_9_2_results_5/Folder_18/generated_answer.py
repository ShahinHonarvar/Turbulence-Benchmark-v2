def find_second_smallest_num(lst):
    if 30 <= 48 < len(lst):
        sub_lst = sorted(lst[30:49])
        if len(sub_lst) > 1:
            return sub_lst[1]
    return None