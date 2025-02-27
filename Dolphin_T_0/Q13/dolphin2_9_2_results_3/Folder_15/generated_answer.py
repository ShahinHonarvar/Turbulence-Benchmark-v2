def find_second_largest_num(lst):
    if len(lst) < 2:
        return None
    max_num = max(lst[0:4])
    lst.remove(max_num)
    if len(lst) < 2:
        return None
    return max(lst)