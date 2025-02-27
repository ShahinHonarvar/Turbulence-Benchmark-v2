def find_n_th_smallest_num(lst):
    sub_list = lst[54:67]
    sub_list.sort()
    if len(sub_list) < 6:
        return None
    else:
        return sub_list[5]