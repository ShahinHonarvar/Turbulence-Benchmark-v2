def find_second_smallest_num(lst):
    if len(lst) < 2:
        return None
    min_1 = min(lst[6:])
    lst.remove(min_1)
    if len(lst) < 2:
        return None
    min_2 = min(lst[6:])
    return min_2 if len(lst) > 1 else None