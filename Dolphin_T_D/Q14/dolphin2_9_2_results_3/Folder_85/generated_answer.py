def find_second_smallest_num(input_list):
    if len(input_list) < 2:
        return None
    smallest_num = float('inf')
    second_smallest_num = float('inf')
    for i in range(len(input_list)):
        if input_list[i] < smallest_num:
            second_smallest_num = smallest_num
            smallest_num = input_list[i]
        elif input_list[i] < second_smallest_num and input_list[i] != smallest_num:
            second_smallest_num = input_list[i]
    if second_smallest_num == float('inf'):
        return None
    else:
        return second_smallest_num