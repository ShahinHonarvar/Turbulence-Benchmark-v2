def find_largest_num(lst):
    max_num = None
    for i in range(10, 101):
        if max_num is None or lst[i] > max_num:
            max_num = lst[i]
    return max_num