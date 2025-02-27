def find_second_smallest_num(lst):
    sub_lst = lst[62:79]
    if len(sub_lst) < 2:
        return None
    min_num = min(sub_lst)
    sub_lst.remove(min_num)
    second_min_num = min(sub_lst)
    second_min_num = lst.index(second_min_num)
    return second_min_num