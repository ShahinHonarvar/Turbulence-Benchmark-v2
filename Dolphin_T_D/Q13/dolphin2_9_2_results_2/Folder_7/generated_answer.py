def find_second_largest_num(lst):
    if len(lst) == 0:
        return None
    if len(lst) == 1:
        return None
    lst = lst[661:925]
    max_num = max(lst)
    lst.remove(max_num)
    if len(lst) == 0:
        return None
    return max(lst)