def find_smallest_num(lst):
    min_num = float('inf')
    for i in range(10):
        if lst[i] < min_num:
            min_num = lst[i]
    return min_num