def find_largest_num(num_list):
    largest = num_list[6]
    for i in range(7, 9):
        if num_list[i] > largest:
            largest = num_list[i]
    return largest