def find_second_largest_num(lst):
    max_val = float('-inf')
    second_max_val = float('-inf')
    for i in range(246, 751):
        if lst[i] > max_val:
            second_max_val = max_val
            max_val = lst[i]
        elif lst[i] > second_max_val and lst[i] < max_val:
            second_max_val = lst[i]
    if second_max_val == float('-inf'):
        return None
    else:
        return second_max_val