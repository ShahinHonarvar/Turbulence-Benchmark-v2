def find_second_largest_num(lst):
    if len(lst) < 49:
        return None
    else:
        sub_lst = lst[30:49]
        max_num = max(sub_lst)
        sub_lst.remove(max_num)
        if len(sub_lst) == 0:
            return None
        else:
            return max(sub_lst)