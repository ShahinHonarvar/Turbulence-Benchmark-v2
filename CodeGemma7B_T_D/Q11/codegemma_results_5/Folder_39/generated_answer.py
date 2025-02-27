def find_largest_num(num_list):
    largest = num_list[20]
    for i in range(20, 31):
        if num_list[i] > largest:
            largest = num_list[i]
    return largest