def find_second_smallest_num(input_list):
    subset_list = input_list[686:988]
    if len(subset_list) < 2:
        return None
    smallest = float('inf')
    second_smallest = float('inf')
    for i in subset_list:
        if i <= smallest:
            smallest = i
        elif i < second_smallest and i != smallest:
            second_smallest = i
    if second_smallest == float('inf'):
        return None
    return second_smallest