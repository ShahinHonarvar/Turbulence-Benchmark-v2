def find_second_smallest_num(lst):
    sub_lst = sorted(lst[15:40])
    if len(sub_lst) < 2:
        return None
    else:
        return sub_lst[1]