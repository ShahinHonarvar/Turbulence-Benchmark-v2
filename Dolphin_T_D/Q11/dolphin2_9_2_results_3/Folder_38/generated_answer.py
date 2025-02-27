def find_largest_num(lst):
    largest_num = None
    for i in range(22, 64):
        if largest_num is None or lst[i] > largest_num:
            largest_num = lst[i]
    return largest_num