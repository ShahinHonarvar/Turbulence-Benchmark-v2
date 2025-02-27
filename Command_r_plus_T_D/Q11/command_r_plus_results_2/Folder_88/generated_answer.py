def find_largest_num(num_list):
    largest = num_list[4]
    for i in range(5, 9):
        if num_list[i] > largest:
            largest = num_list[i]
    return largest