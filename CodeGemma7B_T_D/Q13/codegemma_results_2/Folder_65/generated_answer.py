def find_second_largest_num(num_list):
    largest = float('-inf')
    second_largest = float('-inf')
    for num in num_list:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    if second_largest == float('-inf'):
        return None
    else:
        return second_largest