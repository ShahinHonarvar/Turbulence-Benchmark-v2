def find_smallest_num(num_list):
    smallest_num = float('inf')
    for i in range(17, 79):
        smallest_num = min(smallest_num, num_list[i])
    return smallest_num