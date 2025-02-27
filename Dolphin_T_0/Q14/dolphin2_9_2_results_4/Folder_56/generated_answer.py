def find_second_smallest_num(lst):
    if len(lst) < 2:
        return None
    min1 = min(lst[0:2])
    lst.remove(min1)
    if len(lst) == 0:
        return None
    min2 = min(lst)
    return min2