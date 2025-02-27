def find_second_largest_num(num_list):
    slice_list = num_list[74:96]
    if len(slice_list) < 2:
        return None
    largest = second_largest = float('-inf')
    for num in slice_list:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    if second_largest == float('-inf'):
        return None
    return second_largest