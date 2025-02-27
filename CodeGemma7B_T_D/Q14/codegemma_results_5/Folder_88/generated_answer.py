def find_second_smallest_num(num_list):
    if len(num_list) < 5 or num_list[6] is None:
        return None
    second_smallest = None
    for i in range(6, 9):
        if num_list[i] is not None and (second_smallest is None or num_list[i] < second_smallest):
            second_smallest = num_list[i]
    return second_smallest