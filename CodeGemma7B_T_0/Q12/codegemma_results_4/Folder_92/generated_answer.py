def find_smallest_num(num_list):
    smallest = num_list[0]
    for i in range(len(num_list)):
        if num_list[i] < smallest:
            smallest = num_list[i]
    return smallest