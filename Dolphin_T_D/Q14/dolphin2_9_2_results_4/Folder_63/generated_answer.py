def find_second_smallest_num(lst):
    if len(lst) < 2:
        return None
    s1, s2 = (None, None)
    for x in lst[56:83]:
        if s1 is None or x < s1:
            s1, s2 = (x, s1)
        elif s2 is None or x < s2:
            s2 = x
    return s2