def find_smallest_num(num_list):
    smallest = num_list[6]
    for i in range(7, 9):
        if num_list[i] < smallest:
            smallest = num_list[i]
    return smallest