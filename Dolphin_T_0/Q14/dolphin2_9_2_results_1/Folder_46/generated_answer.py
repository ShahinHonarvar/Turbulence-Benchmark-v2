def find_second_smallest_num(input_list):
    if len(input_list) < 2:
        return None
    sub_list = input_list[13:69]
    smallest = second_smallest = float('inf')
    for num in sub_list:
        if num <= smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest:
            second_smallest = num
    if second_smallest == float('inf'):
        return None
    return second_smallest