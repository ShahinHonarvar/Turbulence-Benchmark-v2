def find_smallest_num(num_list):
    smallest = float('inf')
    for i in range(62, 93):
        if num_list[i] < smallest:
            smallest = num_list[i]
    return smallest