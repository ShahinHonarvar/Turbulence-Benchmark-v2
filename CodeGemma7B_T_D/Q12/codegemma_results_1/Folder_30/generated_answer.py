def find_smallest_num(some_list):
    min_num = float('inf')
    for i in range(29, 52):
        min_num = min(min_num, some_list[i])
    return min_num