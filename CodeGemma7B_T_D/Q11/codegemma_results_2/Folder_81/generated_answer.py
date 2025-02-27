def find_largest_num(num_list):
    max_num = float('-inf')
    for i in range(10, 101):
        if num_list[i] > max_num:
            max_num = num_list[i]
    return max_num