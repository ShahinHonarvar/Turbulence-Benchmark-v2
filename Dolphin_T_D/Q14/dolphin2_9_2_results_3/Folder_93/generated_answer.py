def find_second_smallest_num(arr):
    if 75 < len(arr) < 88:
        arr = arr[75:88 + 1]
        if len(arr) < 2:
            return None
        m1, m2 = (float('inf'), float('inf'))
        for x in arr:
            if x <= m1:
                m1, m2 = (x, m1)
            elif x < m2:
                m2 = x
        return m2 if m2 != float('inf') else None
    else:
        return None