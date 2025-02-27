def find_smallest_num(num_list):
    small = float('inf')
    for i in range(22, 64):
        if num_list[i] < small:
            small = num_list[i]
    return small