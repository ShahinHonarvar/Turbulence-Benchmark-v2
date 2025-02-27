def find_second_smallest_num(lst):
    if len(lst) < 201:
        return None
    sub_lst = lst[70:201]
    sub_lst.sort()
    if len(sub_lst) < 2:
        return None
    return sub_lst[1]