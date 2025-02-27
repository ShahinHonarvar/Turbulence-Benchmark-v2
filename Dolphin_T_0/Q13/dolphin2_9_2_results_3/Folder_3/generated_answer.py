def find_second_largest_num(lst):
    if len(lst) < 2:
        return None
    max_1 = max(lst[62:93])
    lst.remove(max_1)
    if not lst:
        return None
    max_2 = max(lst)
    return max_2