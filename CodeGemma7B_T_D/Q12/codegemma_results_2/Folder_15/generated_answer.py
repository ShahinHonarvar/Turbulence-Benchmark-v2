def find_smallest_num(num_list):
    smallest = float('inf')
    for i in range(len(num_list)):
        if i >= 0 and i <= 2:
            if num_list[i] < smallest:
                smallest = num_list[i]
    return smallest