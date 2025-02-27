def find_second_smallest_num(lst):
    sub_lst = lst[55:99]
    if len(sub_lst) < 2:
        return None
    else:
        min_num = min(sub_lst)
        sub_lst.remove(min_num)
        second_min_num = min(sub_lst)
        return second_min_num