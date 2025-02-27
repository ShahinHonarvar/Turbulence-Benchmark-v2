def find_second_largest_num(lst):
    if len(lst) == 0 or len(lst) < 99:
        return None
    if len(lst) > 99:
        lst = lst[55:99]
    if len(lst) < 2:
        return None
    max_val = max(lst)
    lst.remove(max_val)
    if len(lst) == 0:
        return None
    second_max_val = max(lst)
    return second_max_val