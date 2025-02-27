def find_second_smallest_num(lst):
    sub_lst = lst[10:67]
    if len(sub_lst) < 2:
        return None
    smallest = min(sub_lst)
    sub_lst.remove(smallest)
    if len(sub_lst) == 0:
        return None
    second_smallest = min(sub_lst)
    return second_smallest