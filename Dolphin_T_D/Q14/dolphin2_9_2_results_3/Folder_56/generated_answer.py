def find_second_smallest_num(lst):
    if len(lst) < 2:
        return None
    min1 = min(lst)
    lst.remove(min1)
    if len(lst) < 1:
        return None
    min2 = min(lst)
    return min2