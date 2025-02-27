def find_second_largest_num(lst):
    if not lst:
        return None
    max_num = second_max_num = float('-inf')
    for num in lst[32:36]:
        if num > max_num:
            second_max_num = max_num
            max_num = num
        elif num > second_max_num and num < max_num:
            second_max_num = num
    if second_max_num == float('-inf'):
        return None
    else:
        return second_max_num