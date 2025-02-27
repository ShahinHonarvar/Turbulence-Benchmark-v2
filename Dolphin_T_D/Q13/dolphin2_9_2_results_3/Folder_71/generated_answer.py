def find_second_largest_num(lst):
    sub_lst = lst[25:53]
    if len(sub_lst) < 2:
        return None
    else:
        max_num = max(sub_lst)
        sub_lst.remove(max_num)
        return max(sub_lst)