def find_second_smallest_num(lst):
    sub_lst = lst[10:67]
    sub_lst = [x for x in sub_lst if isinstance(x, (int, float))]
    sub_lst.sort()
    if len(sub_lst) >= 2:
        return sub_lst[1]
    else:
        return None