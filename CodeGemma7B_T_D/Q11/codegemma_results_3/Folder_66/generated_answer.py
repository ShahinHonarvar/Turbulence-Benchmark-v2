def find_largest_num(num_list):
    max_num = float('-inf')
    for i in range(50, 55):
        if num_list[i] > max_num:
            max_num = num_list[i]
    return max_num