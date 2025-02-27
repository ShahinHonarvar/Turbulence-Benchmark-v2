def find_second_smallest_num(input_list):
    if len(input_list) == 0:
        return None
    if len(input_list) < 2:
        return None
    second_smallest = None
    smallest = None
    for i in range(60, 201):
        if smallest is None or smallest > input_list[i]:
            second_smallest = smallest
            smallest = input_list[i]
        elif second_smallest is None or second_smallest > input_list[i]:
            second_smallest = input_list[i]
    return second_smallest