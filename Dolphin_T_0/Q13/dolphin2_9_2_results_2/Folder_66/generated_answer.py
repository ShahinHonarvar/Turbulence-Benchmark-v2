def find_second_largest_num(lst):
    if len(lst) < 5:
        return None
    lst = lst[49:55]
    if len(lst) < 2:
        return None
    max1 = max(lst)
    lst.remove(max1)
    return max(lst) if len(lst) > 1 else None