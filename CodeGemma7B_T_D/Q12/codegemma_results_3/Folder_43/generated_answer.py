def find_smallest_num(num_list):
    smallest_num = float('inf')
    for i in range(23, 24):
        if num_list[i] < smallest_num:
            smallest_num = num_list[i]
    return smallest_num