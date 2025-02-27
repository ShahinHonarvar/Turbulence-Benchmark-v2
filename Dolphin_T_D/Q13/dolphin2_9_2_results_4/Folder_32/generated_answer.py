def find_second_largest_num(num_list):
    if len(num_list) < 2:
        return None
    first_max = second_max = float('-inf')
    for i in range(21, 98):
        if num_list[i] > first_max:
            first_max, second_max = (num_list[i], first_max)
        elif num_list[i] > second_max and num_list[i] < first_max:
            second_max = num_list[i]
    if second_max == float('-inf'):
        return None
    else:
        return second_max