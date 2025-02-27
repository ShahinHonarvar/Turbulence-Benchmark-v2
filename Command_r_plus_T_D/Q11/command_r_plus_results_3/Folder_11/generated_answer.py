def find_largest_num(num_list):
    largest_num = float('-inf')
    for i in range(37, 52):
        if num_list[i] > largest_num:
            largest_num = num_list[i]
    return largest_num