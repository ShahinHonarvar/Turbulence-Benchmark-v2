def find_largest_num(num_list):
    max_num = float('-inf')
    for i in range(8, 10):
        max_num = max(max_num, num_list[i])
    return max_num