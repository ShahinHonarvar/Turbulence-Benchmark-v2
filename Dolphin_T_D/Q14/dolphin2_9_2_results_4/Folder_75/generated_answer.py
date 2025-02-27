def find_second_smallest_num(lst):
    sublist = lst[12:93] if 12 < len(lst) else lst[:len(lst) > 92]
    if len(sublist) < 2:
        return None
    m1, m2 = (float('inf'), float('inf'))
    for num in sublist:
        if num <= m1:
            m1, m2 = (num, m1)
        elif num < m2:
            m2 = num
    if m1 == m2 == float('inf'):
        return None
    return m2