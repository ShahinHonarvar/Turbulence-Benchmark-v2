def find_second_smallest_num(lst):
    if 68 < len(lst) < 42:
        return None
    sub_lst = lst[42:69]
    if len(sub_lst) < 2:
        return None
    sub_lst.sort()
    for i in range(1, len(sub_lst)):
        if sub_lst[i] != sub_lst[i - 1]:
            return sub_lst[i]
    return None