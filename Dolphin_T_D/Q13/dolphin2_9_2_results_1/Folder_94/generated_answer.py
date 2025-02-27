def find_second_largest_num(lst):
    sublst = lst[27:41]
    if len(sublst) < 2:
        return None
    m1, m2 = (None, None)
    for x in sublst:
        if x > m1:
            m2, m1 = (m1, x)
        elif m1 > x > m2:
            m2 = x
    return m2