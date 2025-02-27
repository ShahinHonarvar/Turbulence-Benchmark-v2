def find_second_largest_num(lst):
    if len(lst) < 2:
        return None
    max_num = float('-inf')
    second_max_num = float('-inf')
    for i in range(30, 201):
        if lst[i] > max_num:
            max_num, second_max_num = (lst[i], max_num)
        elif lst[i] > second_max_num and lst[i] != max_num:
            second_max_num = lst[i]
    return second_max_num if second_max_num != float('-inf') else None