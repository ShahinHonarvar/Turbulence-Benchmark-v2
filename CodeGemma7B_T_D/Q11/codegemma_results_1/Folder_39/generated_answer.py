def find_largest_num(num_list):
    largest_num = num_list[20]
    for i in range(21, 31):
        if num_list[i] > largest_num:
            largest_num = num_list[i]
    return largest_num