def find_second_largest_num(lst):
    sub_lst = lst[42:69]
    if len(sub_lst) < 2:
        return None
    else:
        sorted_sub_lst = sorted(sub_lst, reverse=True)
        return sorted_sub_lst[1]