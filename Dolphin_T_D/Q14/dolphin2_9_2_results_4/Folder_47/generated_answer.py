def find_second_smallest_num(lst):
    sl = lst[22:64]
    if len(sl) == 1:
        return None
    min1 = min(sl)
    sl.remove(min1)
    if len(sl) == 1:
        return None
    min2 = min(sl)
    return min2