def find_second_smallest_num(lst):
    sub_lst = sorted(lst[66:94])
    if len(sub_lst) >= 2:
        return sub_lst[1]
    else:
        return None