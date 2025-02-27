def find_second_smallest_num(lst):
    sub_lst = lst[55:99] if isinstance(lst, list) else list()
    if len(sub_lst) < 2:
        return 'None'
    else:
        sub_lst.sort()
        return sub_lst[1]