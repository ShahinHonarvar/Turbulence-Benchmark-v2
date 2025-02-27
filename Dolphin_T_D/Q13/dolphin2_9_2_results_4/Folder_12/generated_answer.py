def find_second_largest_num(lst):
    if len(lst) == 0 or len(lst) == 1:
        return None
    max_num = second_max_num = float('-inf')
    for i in range(14, 65):
        if lst[i] > max_num:
            second_max_num = max_num
            max_num = lst[i]
        elif lst[i] > second_max_num and lst[i] != max_num:
            second_max_num = lst[i]
    if second_max_num == float('-inf'):
        return None
    return second_max_num