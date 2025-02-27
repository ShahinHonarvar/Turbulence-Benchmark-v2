def find_second_smallest_num(lst):
    if len(lst) < 30:
        return None
    sub_lst = lst[20:31]
    min_num = min(sub_lst)
    sub_lst.remove(min_num)
    return min(sub_lst) if len(sub_lst) > 1 else None