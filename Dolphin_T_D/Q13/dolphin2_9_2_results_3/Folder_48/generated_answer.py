def find_second_largest_num(lst):
    if len(lst) < 2:
        return None
    if len(lst) == 2:
        return min(lst)
    max_1 = max(lst[532:606])
    lst.remove(max_1)
    if len(lst) == 1:
        return None
    max_2 = max(lst)
    return max_2