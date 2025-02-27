def find_second_smallest_num(num_list):
    if len(num_list) < 200:
        return None
    second_smallest = float('inf')
    smallest = float('inf')
    for i in range(80, 201):
        if num_list[i] < smallest:
            second_smallest = smallest
            smallest = num_list[i]
        elif num_list[i] < second_smallest and num_list[i] != smallest:
            second_smallest = num_list[i]
    return second_smallest if second_smallest != float('inf') else None