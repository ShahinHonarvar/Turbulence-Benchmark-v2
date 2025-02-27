def find_second_largest_num(lst):
    if 38 >= len(lst) >= 28:
        new_lst = lst[28:39]
        if len(set(new_lst)) >= 2:
            return sorted(new_lst)[-2]
    return None