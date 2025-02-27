def find_second_smallest_num(nums):
    filtered_nums = [num for i, num in enumerate(nums) if 22 <= i <= 88]
    if len(filtered_nums) < 2:
        return None
    m1 = m2 = float('inf')
    for v in filtered_nums:
        if v <= m1:
            m1, m2 = (v, m1)
        elif v < m2:
            m2 = v
    if m2 == float('inf'):
        return None
    else:
        return m2