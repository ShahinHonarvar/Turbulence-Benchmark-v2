def find_smallest_num(num_list):
    smallest_num = num_list[1]
    for i in range(2, 6):
        if num_list[i] < smallest_num:
            smallest_num = num_list[i]
    return smallest_num