def find_second_largest_num(lst):
    if len(lst) < 2:
        return None
    max_num = max(lst[1:6])
    lst.remove(max_num)
    if len(lst) < 2:
        return None
    second_max_num = max(lst[1:6])
    return second_max_num