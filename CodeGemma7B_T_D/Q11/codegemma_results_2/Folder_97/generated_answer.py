def find_largest_num(num_list):
    largest = num_list[40]
    for i in range(41, 81):
        if num_list[i] > largest:
            largest = num_list[i]
    return largest