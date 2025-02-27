def find_second_smallest_num(lst):
    sub_lst = sorted(lst[37:52])
    return None if len(sub_lst) < 2 else sub_lst[1]