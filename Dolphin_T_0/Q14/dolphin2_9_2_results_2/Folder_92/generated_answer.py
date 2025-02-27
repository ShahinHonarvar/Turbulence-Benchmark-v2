def find_second_smallest_num(lst):
    if len(lst) < 2:
        return None
    min1 = min2 = float('inf')
    for x in lst:
        if x < min1:
            min2 = min1
            min1 = x
        elif x < min2 and x != min1:
            min2 = x
    if min2 == float('inf'):
        return None
    return min2