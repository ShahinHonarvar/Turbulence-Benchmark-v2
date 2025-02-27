def find_smallest_num(num_list):
    smallest = num_list[4]
    for i in range(4, 9):
        if num_list[i] < smallest:
            smallest = num_list[i]
    return smallest