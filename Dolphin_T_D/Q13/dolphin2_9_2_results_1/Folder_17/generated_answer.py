def find_second_largest_num(lst):
    if not lst:
        return None
    max_num = float('-inf')
    second_max = float('-inf')
    for i in range(62, 79):
        if lst[i] > max_num and i < len(lst):
            second_max = max_num
            max_num = lst[i]
        elif lst[i] > second_max and lst[i] != max_num and (i < len(lst)):
            second_max = lst[i]
    if max_num == second_max:
        return None
    return second_max