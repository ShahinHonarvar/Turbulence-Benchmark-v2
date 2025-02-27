def find_second_largest_num(lst):
    if len(lst) < 2:
        return None
    max_num1 = float('-inf')
    max_num2 = float('-inf')
    for i in lst[29:80]:
        if i > max_num1:
            max_num2 = max_num1
            max_num1 = i
        elif i > max_num2 and i != max_num1:
            max_num2 = i
    if max_num2 == float('-inf'):
        return None
    return max_num2