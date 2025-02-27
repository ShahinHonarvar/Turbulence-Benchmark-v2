def find_second_smallest_num(lst):
    if not lst:
        return None
    sublist = lst[70:201]
    if len(sublist) < 2:
        return None
    m1, m2 = (sublist[0], sublist[1])
    for i in range(1, len(sublist)):
        if sublist[i] < m2:
            m1, m2 = (m2, sublist[i])
        if sublist[i] < m1:
            m2 = m1
            m1 = sublist[i]
    return m2