def find_second_smallest_num(numbers):
    branch = numbers[62:79]
    if len(branch) < 2:
        return None
    m1, m2 = (float('inf'), float('inf'))
    for x in branch:
        if x <= m1:
            m1, m2 = (x, m1)
        elif x < m2:
            m2 = x
    return m2 if m2 != float('inf') else None