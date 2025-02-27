def find_second_largest_num(lst):
    if len(lst) < 2:
        return None
    lst = lst[31:34]
    max_num = max(lst)
    lst.remove(max_num)
    if len(lst) < 2:
        return None
    return max(lst)