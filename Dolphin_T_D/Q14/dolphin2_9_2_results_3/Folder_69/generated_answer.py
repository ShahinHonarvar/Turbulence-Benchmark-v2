def find_second_smallest_num(lst):
    sub_lst = lst[25:88]
    if len(sub_lst) < 2:
        return None
    sub_lst.sort()
    for i in range(1, len(sub_lst)):
        if sub_lst[i] != sub_lst[0]:
            return sub_lst[i]
    return None