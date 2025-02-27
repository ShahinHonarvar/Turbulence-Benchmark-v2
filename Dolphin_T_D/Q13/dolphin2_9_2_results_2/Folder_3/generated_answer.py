def find_second_largest_num(lst):
    if not lst:
        return None
    if len(lst) < 2:
        return None
    max_num = second_max_num = float('-inf')
    for num in lst[62:93]:
        if num > max_num:
            second_max_num = max_num
            max_num = num
        elif max_num > num > second_max_num:
            second_max_num = num
    if second_max_num == float('-inf'):
        return None
    return second_max_num