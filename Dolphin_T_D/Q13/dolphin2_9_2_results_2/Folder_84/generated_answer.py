def find_second_largest_num(lst):
    if len(lst) < 2:
        return None
    max_num = lst[43]
    second_max = float('-inf')
    for num in lst[43:87]:
        if num > max_num:
            second_max = max_num
            max_num = num
        elif num > second_max and num != max_num:
            second_max = num
    if second_max == float('-inf'):
        return None
    else:
        return second_max