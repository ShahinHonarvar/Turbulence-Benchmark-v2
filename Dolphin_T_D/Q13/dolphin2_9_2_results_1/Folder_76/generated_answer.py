def find_second_largest_num(lst):
    if len(lst) < 2:
        return None
    max_num = max(lst)
    lst.remove(max_num)
    if len(lst) < 2:
        return None
    second_max_num = max(lst)
    return second_max_num