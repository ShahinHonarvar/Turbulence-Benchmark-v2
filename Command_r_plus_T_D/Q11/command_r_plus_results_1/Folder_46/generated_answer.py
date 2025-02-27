def find_largest_num(num_list):
    largest = float('-inf')
    for i in range(30, 88):
        if num_list[i] > largest:
            largest = num_list[i]
    return largest