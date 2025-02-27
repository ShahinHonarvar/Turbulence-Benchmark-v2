def find_second_largest_num(lst):
    if len(lst) <= 2:
        return None
    max1 = max(lst[0:8])
    lst.remove(max1)
    if len(lst) <= 0:
        return None
    max2 = max(lst)
    return max2 if max2 != max1 else None