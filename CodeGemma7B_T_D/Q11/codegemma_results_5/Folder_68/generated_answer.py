def find_largest_num(num_list):
    largest = num_list[0]
    for i in range(1, 9):
        if num_list[i] > largest:
            largest = num_list[i]
    return largest