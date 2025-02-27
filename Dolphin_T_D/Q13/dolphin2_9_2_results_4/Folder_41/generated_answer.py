def find_second_largest_num(lst):
    if len(lst) < 2:
        return None
    max_num = second_max = float('-inf')
    for i in lst:
        if i > max_num:
            second_max = max_num
            max_num = i
        elif i > second_max and i != max_num:
            second_max = i
    if second_max == float('-inf'):
        return None
    else:
        return second_max