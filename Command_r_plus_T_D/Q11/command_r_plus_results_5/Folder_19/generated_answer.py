def find_largest_num(num_list):
    largest = num_list[3]
    for i in range(4, 6):
        if num_list[i] > largest:
            largest = num_list[i]
    return largest