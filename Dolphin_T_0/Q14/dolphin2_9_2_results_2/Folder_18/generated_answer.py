def find_second_smallest_num(lst):
    if 48 < len(lst) == 30:
        sub_lst = lst[30:48]
        if len(set(sub_lst)) < 2:
            return None
        min_num = min(sub_lst)
        sub_lst.remove(min_num)
        return min(sub_lst)
    else:
        return None