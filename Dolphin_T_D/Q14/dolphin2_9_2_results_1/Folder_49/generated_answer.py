def find_second_smallest_num(ls):
    s = ls[80:201]
    if len(s) < 2:
        return None
    m1, m2 = (float('inf'), float('inf'))
    for i in s:
        if i <= m1:
            m1, m2 = (i, m1)
        elif i < m2:
            m2 = i
    return m2 if m2 != float('inf') else None