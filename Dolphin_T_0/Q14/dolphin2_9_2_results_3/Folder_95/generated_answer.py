def find_second_smallest_num(lst):
    if len(lst) > 85:
        sub_lst = lst[75:86]
        sub_lst = list(set(sub_lst))
        if len(sub_lst) > 1:
            sub_lst.sort()
            return sub_lst[1]
    return None