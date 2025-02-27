def find_second_smallest_num(lst):
    sublst = lst[59:98]
    if len(sublst) < 2:
        return None
    else:
        m1, m2 = (float('inf'), float('inf'))
        for x in sublst:
            if x <= m1:
                m1, m2 = (x, m1)
            elif x < m2:
                m2 = x
        return m2 if m2 < float('inf') else None