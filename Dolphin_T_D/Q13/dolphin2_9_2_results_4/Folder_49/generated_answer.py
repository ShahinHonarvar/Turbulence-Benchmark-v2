def find_second_largest_num(lst):
    sub_lst = lst[80:201]
    if len(sub_lst) < 2:
        return None
    max_num = max(sub_lst)
    sub_lst.remove(max_num)
    second_max_num = max(sub_lst)
    if second_max_num == max_num:
        return None
    else:
        return second_max_num