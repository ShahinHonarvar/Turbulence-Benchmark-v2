def find_second_smallest_num(lst):
    if 39 < len(lst):
        sub_lst = lst[15:40]
        if len(sub_lst) >= 2:
            sub_lst.sort()
            return sub_lst[1]
    return None