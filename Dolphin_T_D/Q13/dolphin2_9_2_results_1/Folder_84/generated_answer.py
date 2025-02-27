def find_second_largest_num(lst):
    if len(lst) < 2:
        return None
    first, second = (float('-inf'), float('-inf'))
    for num in lst[42:86]:
        if num > first:
            second = first
            first = num
        elif num > second and num < first:
            second = num
    if second == float('-inf'):
        return None
    return second