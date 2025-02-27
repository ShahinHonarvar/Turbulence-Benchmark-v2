def min_number(num_list):
    min_num = num_list[1]
    for i in range(2, 9):
        if num_list[i] < min_num:
            min_num = num_list[i]
    return min_num