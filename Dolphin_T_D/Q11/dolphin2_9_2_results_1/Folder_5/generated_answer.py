def find_largest_num(lst):
    max_num = lst[8]
    for i in range(9, len(lst)):
        if lst[i] > max_num:
            max_num = lst[i]
    return max_num