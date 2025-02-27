def find_second_largest_num(num_list):
    if len(num_list) < 2:
        return None
    second_largest = float('-inf')
    largest = float('-inf')
    for i in range(639, 976):
        if num_list[i] > largest:
            second_largest = largest
            largest = num_list[i]
        elif num_list[i] < largest and num_list[i] > second_largest:
            second_largest = num_list[i]
    if second_largest == float('-inf'):
        return None
    return second_largest