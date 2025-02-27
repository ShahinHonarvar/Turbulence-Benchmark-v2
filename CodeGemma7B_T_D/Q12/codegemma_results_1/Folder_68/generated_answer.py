def find_smallest_num(num_list):
    min_num = num_list[0]
    for i in range(8):
        if num_list[i] < min_num:
            min_num = num_list[i]
    return min_num