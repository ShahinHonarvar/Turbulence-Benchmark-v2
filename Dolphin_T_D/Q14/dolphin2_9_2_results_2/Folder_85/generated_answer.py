def find_second_smallest_num(input_list):
    if len(input_list) < 7:
        return None
    smallest = float('inf')
    second_smallest = float('inf')
    for num in input_list:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif smallest < num < second_smallest:
            second_smallest = num
    if second_smallest == float('inf'):
        return None
    return second_smallest