def find_second_largest_num(lst):
    if not 61 >= len(lst) > 16:
        return None
    lst = lst[15:62]
    if len(lst) < 2:
        return None
    max_num = max(lst)
    lst.remove(max_num)
    if len(lst) == 1:
        return None
    second_max = max(lst)
    return second_max