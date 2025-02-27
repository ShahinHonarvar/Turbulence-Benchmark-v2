def find_second_smallest_num(num_list):
    sub_list = num_list[68:87]
    if len(sub_list) < 2:
        return None
    smallest = second_smallest = float('inf')
    for num in sub_list:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num
    return None if second_smallest == float('inf') else second_smallest