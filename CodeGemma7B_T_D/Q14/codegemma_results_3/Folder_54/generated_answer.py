def find_second_smallest_num(num_list):
    for i in range(68, 87):
        if i < len(num_list):
            element = num_list[i]
            if element < second_smallest or second_smallest == 'None':
                second_smallest = element
    return second_smallest