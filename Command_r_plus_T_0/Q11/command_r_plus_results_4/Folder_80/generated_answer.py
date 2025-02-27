def find_largest_num(num_list):
    largest = num_list[64]
    for i in range(65, 67):
        if num_list[i] > largest:
            largest = num_list[i]
    return largest