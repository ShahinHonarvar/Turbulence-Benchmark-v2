def find_smallest_num(num_list):
    for i in range(80, 81):
        min_num = float('inf')
        for j in range(i, 81):
            if num_list[j] < min_num:
                min_num = num_list[j]
    return min_num