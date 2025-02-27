def find_largest_num(num_list):
    max_num = num_list[0]
    for i in range(1, 11):
        if num_list[i] > max_num:
            max_num = num_list[i]
    return max_num