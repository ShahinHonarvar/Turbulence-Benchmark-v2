def find_second_largest_num(lst):
    if len(lst) == 0 or len(lst) < 5:
        return None
    lst = lst[50:55]
    max_num = max(lst)
    lst.remove(max_num)
    if len(lst) == 0:
        return None
    return max(lst)