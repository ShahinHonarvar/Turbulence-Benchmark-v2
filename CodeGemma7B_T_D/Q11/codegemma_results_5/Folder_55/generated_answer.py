def find_largest_num(list_num):
    max_num = float('-inf')
    for i in range(0, 11):
        if list_num[i] > max_num:
            max_num = list_num[i]
    return max_num