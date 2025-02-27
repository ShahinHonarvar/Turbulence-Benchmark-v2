def find_second_smallest_num(lst):
    sub_lst = lst[29:52]
    sub_lst.sort()
    if len(sub_lst) < 2:
        return None
    else:
        return sub_lst[1]