def find_second_largest_num(lst):
    sub_lst = lst[262:747]
    sub_lst.sort(reverse=True)
    if len(sub_lst) >= 2:
        return sub_lst[1]
    else:
        return None