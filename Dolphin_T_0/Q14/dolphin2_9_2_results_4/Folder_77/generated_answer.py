def find_second_smallest_num(lst):
    lst = lst[639:976]
    if len(lst) == 0:
        return None
    min1, min2 = (float('inf'), float('inf'))
    for i in lst:
        if i <= min1:
            min1, min2 = (i, min1)
        elif i < min2:
            min2 = i
    if min2 == float('inf'):
        return None
    return min2