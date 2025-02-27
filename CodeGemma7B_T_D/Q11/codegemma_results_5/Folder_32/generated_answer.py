def find_largest_num(num_list):
    largest = num_list[21]
    for i in range(22, 98):
        if num_list[i] > largest:
            largest = num_list[i]
    return largest