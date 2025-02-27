def find_largest_num(num_list):
    largest = num_list[75]
    for i in range(76, 95):
        if num_list[i] > largest:
            largest = num_list[i]
    return largest