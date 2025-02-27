def find_second_largest_num(lst):
    sub = lst[50:55]
    if len(sub) < 2:
        return None
    max1 = max(sub)
    sub.remove(max1)
    if len(sub) < 2:
        return None
    return max(sub)