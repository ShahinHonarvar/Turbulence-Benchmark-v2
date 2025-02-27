def find_second_largest_num(lst):
    lst = lst[20:201]
    if len(lst) < 2:
        return None
    max_num = second_max = float('-inf')
    for num in lst:
        if num > max_num:
            second_max = max_num
            max_num = num
        elif num > second_max and num < max_num:
            second_max = num
    return second_max