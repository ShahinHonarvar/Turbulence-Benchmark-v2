def find_second_largest_num(lst):
    if len(lst) <= 51:
        return None
    lst = lst[15:51]
    if len(lst) < 2:
        return None
    max_num = max(lst)
    second_max = float('-inf')
    for i in range(1, len(lst)):
        if lst[i] < max_num and lst[i] > second_max:
            second_max = lst[i]
    if second_max == float('-inf'):
        return 'None'
    else:
        return second_max