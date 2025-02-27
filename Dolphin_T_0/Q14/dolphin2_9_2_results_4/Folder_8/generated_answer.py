def find_second_smallest_num(lst):
    new_lst = lst[55:67]
    if len(new_lst) < 2:
        return None
    min1 = min(new_lst)
    new_lst.remove(min1)
    if len(new_lst) < 1:
        return None
    min2 = min(new_lst)
    return min2