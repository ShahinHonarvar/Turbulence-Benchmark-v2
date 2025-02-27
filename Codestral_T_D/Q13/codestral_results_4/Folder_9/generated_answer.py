def find_second_largest_num(lst):
    if 200 < len(lst) - 1:
        sub_lst = lst[200:201]
        sub_lst.sort()
        return sub_lst[-2] if len(sub_lst) > 1 else None
    return None