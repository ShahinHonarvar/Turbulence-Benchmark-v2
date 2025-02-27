def find_second_smallest_num(lst):
    if len(lst) < 55:
        return None
    sub_lst = lst[50:55]
    sorted_lst = sorted(sub_lst)
    if len(sorted_lst) < 2:
        return None
    return sorted_lst[1]