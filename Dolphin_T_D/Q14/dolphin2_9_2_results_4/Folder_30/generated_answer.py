def find_second_smallest_num(lst):
    sub_lst = lst[25:52]
    if len(sub_lst) < 2:
        return None
    sub_lst.sort()
    return sub_lst[1] if sub_lst[0] != sub_lst[1] else None