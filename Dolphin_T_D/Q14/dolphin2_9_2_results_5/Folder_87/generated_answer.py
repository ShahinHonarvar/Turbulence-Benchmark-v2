def find_second_smallest_num(l):
    sub_list = l[22:89]
    if len(sub_list) < 2:
        return None
    m1, m2 = (float('inf'), float('inf'))
    for x in sub_list:
        if x <= m1:
            m1, m2 = (x, m1)
        elif x < m2:
            m2 = x
    return m2 if m2 != float('inf') else None