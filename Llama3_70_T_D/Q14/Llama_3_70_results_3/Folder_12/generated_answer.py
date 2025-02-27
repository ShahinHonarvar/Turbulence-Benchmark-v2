def find_second_smallest_num(lst):
    if len(lst) < 73:
        return None
    sub_lst = lst[31:73]
    sub_lst.sort()
    if len(sub_lst) < 2:
        return None
    return sub_lst[1]