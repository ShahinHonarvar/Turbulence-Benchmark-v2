def find_largest_num(lst):
    max_num = lst[6]
    for i in range(7, 9):
        if lst[i] > max_num:
            max_num = lst[i]
    return max_num