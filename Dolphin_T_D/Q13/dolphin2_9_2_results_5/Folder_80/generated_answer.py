def find_second_largest_num(lst):
    if len(lst) < 3:
        return None
    max_num = max(lst[64:67])
    lst.remove(max_num)
    if len(lst) < 2:
        return None
    second_max_num = max(lst[64:67])
    return second_max_num