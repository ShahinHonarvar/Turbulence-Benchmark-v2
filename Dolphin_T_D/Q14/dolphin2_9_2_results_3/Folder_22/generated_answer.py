def find_second_smallest_num(lst):
    sub_lst = lst[40:201]
    if len(sub_lst) < 2:
        return None
    min1 = min(sub_lst)
    sub_lst.remove(min1)
    if len(sub_lst) < 1:
        return None
    min2 = min(sub_lst)
    return min2