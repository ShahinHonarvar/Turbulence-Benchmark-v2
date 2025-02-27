def find_smallest_num(num_list):
    min_num = float('inf')
    for i in range(55, 99):
        min_num = min(min_num, num_list[i])
    return min_num