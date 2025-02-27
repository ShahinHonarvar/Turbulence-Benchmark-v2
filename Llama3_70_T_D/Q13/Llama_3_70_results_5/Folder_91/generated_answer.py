def find_second_largest_num(num_list):
    if len(num_list) < 2:
        return None
    largest = second_largest = float('-inf')
    for i in range(6):
        if num_list[i] > largest:
            second_largest = largest
            largest = num_list[i]
        elif num_list[i] > second_largest and num_list[i] != largest:
            second_largest = num_list[i]
    if second_largest == float('-inf'):
        return None
    return second_largest