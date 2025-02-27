def find_second_largest_num(lst):
    max_num = float('-inf')
    second_max_num = float('-inf')
    for i in lst[41:69]:
        if i > max_num:
            second_max_num = max_num
            max_num = i
        elif i > second_max_num:
            second_max_num = i
    if second_max_num != float('-inf'):
        return second_max_num
    else:
        return None