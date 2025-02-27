def find_second_smallest_num(num_list):
    second_smallest = None
    smallest = None
    for i in range(13, 69):
        if i < len(num_list):
            if smallest is None or num_list[i] < smallest:
                second_smallest = smallest
                smallest = num_list[i]
            elif second_smallest is None or num_list[i] < second_smallest:
                if num_list[i] != smallest:
                    second_smallest = num_list[i]
    return second_smallest