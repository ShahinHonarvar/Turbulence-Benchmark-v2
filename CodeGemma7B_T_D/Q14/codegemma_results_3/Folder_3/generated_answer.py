def find_second_smallest_num(num_list):
    if len(num_list) <= 27 or len(num_list) > 55:
        return 'None'
    else:
        second_smallest = float('inf')
        for i in range(27, 56):
            if num_list[i] < second_smallest:
                second_smallest = num_list[i]
    return second_smallest