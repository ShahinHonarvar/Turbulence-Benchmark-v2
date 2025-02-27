def find_largest_num(lst):
    max_num = lst[0]
    for i in range(1, 4):
        if lst[i] > max_num:
            max_num = lst[i]
    return max_num