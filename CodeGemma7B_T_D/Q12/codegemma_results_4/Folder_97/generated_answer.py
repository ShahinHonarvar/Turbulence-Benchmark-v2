def find_smallest_num(num_list):
    min_num = float('inf')
    for i in range(33, 37):
        if num_list[i] < min_num:
            min_num = num_list[i]
    return min_num