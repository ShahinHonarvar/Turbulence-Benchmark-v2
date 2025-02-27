def find_second_largest_num(lst):
    sub_lst = lst[42:69]
    if len(sub_lst) < 2:
        return None
    else:
        sub_lst.sort()
        return sub_lst[-2]