def find_smallest_num(num_list):
    smallest = num_list[0]
    for i in range(1, 3):
        if num_list[i] < smallest:
            smallest = num_list[i]
    return smallest