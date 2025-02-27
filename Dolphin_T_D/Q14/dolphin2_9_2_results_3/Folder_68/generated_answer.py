def find_second_smallest_num(lst):
    if len(lst) < 9:
        return None
    min1 = min(lst[:9])
    lst.remove(min1)
    if len(lst[:9]) > 0:
        return min(lst[:9])
    else:
        return None