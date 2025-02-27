def find_second_largest_num(lst):
    sub_lst = lst[28:41]
    if len(set(sub_lst)) < 2:
        return None
    else:
        return sorted(sub_lst)[-2]