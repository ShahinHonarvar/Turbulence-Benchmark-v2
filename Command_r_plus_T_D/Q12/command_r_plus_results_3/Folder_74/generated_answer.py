def find_smallest_num(num_list):
    smallest = float('inf')
    for i in range(22, 89):
        if num_list[i] < smallest:
            smallest = num_list[i]
    return smallest