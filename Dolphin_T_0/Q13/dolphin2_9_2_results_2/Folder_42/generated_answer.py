def find_second_largest_num(lst):
    if len(lst) < 2:
        return None
    max1 = max(lst[29:80])
    lst.remove(max1)
    if len(lst) < 2:
        return None
    max2 = max(lst)
    return max2