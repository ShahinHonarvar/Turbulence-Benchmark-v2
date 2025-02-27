def find_second_largest_num(lst):
    if not lst:
        return None
    max_num = float('-inf')
    for i in range(209, 557):
        if lst[i] > max_num:
            max_num = lst[i]
    max_num_index = lst.index(max_num)
    if len(lst) == 1 or max_num_index == 0 or max_num_index == len(lst) - 1:
        return None
    second_max_num = float('-inf')
    for i in range(max_num_index - 1, -1, -1):
        if lst[i] < max_num and lst[i] > second_max_num:
            second_max_num = lst[i]
    if second_max_num == float('-inf'):
        return None
    return second_max_num