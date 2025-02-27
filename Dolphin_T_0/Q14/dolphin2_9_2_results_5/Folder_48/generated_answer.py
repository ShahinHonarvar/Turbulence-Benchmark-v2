def find_second_smallest_num(input_list):
    smallest = float('inf')
    second_smallest = float('inf')
    for i in input_list[246:751]:
        if i < smallest:
            second_smallest = smallest
            smallest = i
        elif i < second_smallest and i != smallest:
            second_smallest = i
    if second_smallest == float('inf'):
        return None
    else:
        return second_smallest