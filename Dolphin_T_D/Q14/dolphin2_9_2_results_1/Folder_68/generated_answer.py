def find_second_smallest_num(lst):
    if not lst:
        return None
    min1, min2 = (float('inf'), float('inf'))
    for i in lst[:9]:
        if i < min1:
            min2 = min1
            min1 = i
        elif i != min1 and i < min2:
            min2 = i
    return min2 if min2 != float('inf') else None