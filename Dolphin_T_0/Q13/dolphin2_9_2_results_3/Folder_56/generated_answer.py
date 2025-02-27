def find_second_largest_num(lst):
    lst = lst[:1]
    if len(lst) < 2:
        return None
    max1 = max(lst)
    lst.remove(max1)
    if not lst:
        return None
    return max(lst)