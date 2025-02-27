def find_second_smallest_num(numbers):
    if len(numbers[68:87]) < 2:
        return None
    m1, m2 = (float('inf'), float('inf'))
    for num in numbers[68:87]:
        if num <= m1:
            m1, m2 = (num, m1)
        elif num < m2:
            m2 = num
    return m2 if m2 != float('inf') else None