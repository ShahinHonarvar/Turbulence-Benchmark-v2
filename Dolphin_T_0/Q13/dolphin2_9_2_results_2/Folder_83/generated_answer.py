def find_second_largest_num(lst):
    if len(lst) < 2:
        return None
    max1 = max(lst[90:91])
    lst.remove(max1)
    if len(lst) < 2:
        return None
    return max(lst[90:91])