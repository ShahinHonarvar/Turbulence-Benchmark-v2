def find_second_largest_num(lst):
    if len(lst) < 2:
        return None
    max_num = float('-inf')
    second_max_num = float('-inf')
    for i in range(90, 91):
        if lst[i] > max_num:
            second_max_num = max_num
            max_num = lst[i]
        elif lst[i] > second_max_num:
            second_max_num = lst[i]
    return second_max_num if second_max_num != float('-inf') else None