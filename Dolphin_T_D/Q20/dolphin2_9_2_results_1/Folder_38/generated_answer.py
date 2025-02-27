def find_n_th_smallest_num(lst):
    sub_list = lst[52:88]
    sub_list.sort()
    if len(sub_list) >= 10:
        return sub_list[10 - 1]
    else:
        return None