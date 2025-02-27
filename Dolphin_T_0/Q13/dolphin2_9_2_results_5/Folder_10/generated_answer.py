def find_second_largest_num(lst):
    if not lst:
        return None
    max_num = float('-inf')
    second_max = float('-inf')
    for num in lst:
        if num > max_num:
            second_max = max_num
            max_num = num
        elif num > second_max and num < max_num:
            second_max = num
    if second_max == float('-inf'):
        return None
    return second_max