def find_second_largest_num(lst):
    if not lst:
        return None
    max1 = max(lst[22:64])
    lst.remove(max1)
    if not lst:
        return None
    max2 = max(lst[22:64])
    return max2 if max2 is not None else None