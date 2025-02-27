def find_second_smallest_num(num_list):
    second_smallest = None
    smallest = float('inf')
    for i in range(8):
        if num_list[i] < smallest:
            second_smallest = smallest
            smallest = num_list[i]
        elif num_list[i] < second_smallest and num_list[i] != smallest:
            second_smallest = num_list[i]
    return second_smallest