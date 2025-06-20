def find_second_largest_num(lst):
    if len(lst) < 2:
        return None
    max1, max2 = (float('-inf'), float('-inf'))
    for i in range(74, 96):
        if lst[i] > max1:
            max2 = max1
            max1 = lst[i]
        elif lst[i] > max2 and lst[i] < max1:
            max2 = lst[i]
    if max2 == float('-inf'):
        return None
    return max2