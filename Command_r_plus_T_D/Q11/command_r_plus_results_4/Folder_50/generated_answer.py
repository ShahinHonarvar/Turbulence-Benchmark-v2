def find_largest_num(num_list):
    start_index = 70
    end_index = 84
    largest_num = float('-inf')
    for i in range(start_index, end_index + 1):
        if num_list[i] > largest_num:
            largest_num = num_list[i]
    return largest_num