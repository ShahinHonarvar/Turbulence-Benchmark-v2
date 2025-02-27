def find_second_largest_num(lst):
    if len(lst) < 2:
        return None
    max_1 = float('-inf')
    max_2 = float('-inf')
    for i in range(36, 47):
        num = lst[i]
        if num > max_1:
            max_2 = max_1
            max_1 = num
        elif num > max_2 and num != max_1:
            max_2 = num
    if max_1 == max_2:
        return None
    return max_2