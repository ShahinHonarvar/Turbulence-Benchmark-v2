def find_second_largest_num(lst):
    lst = lst[62:64]
    if len(lst) < 2:
        return None
    return sorted(lst)[-2]