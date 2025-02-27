def find_smallest_num(num_list):
    smallest = float('inf')
    for i in range(34, 56):
        if num_list[i] < smallest:
            smallest = num_list[i]
    return smallest