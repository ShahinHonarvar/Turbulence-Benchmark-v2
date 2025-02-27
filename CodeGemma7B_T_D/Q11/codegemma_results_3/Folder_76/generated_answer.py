def find_largest_num(num_list):
    largest_num = num_list[686]
    for i in range(687, 988):
        if num_list[i] > largest_num:
            largest_num = num_list[i]
    return largest_num