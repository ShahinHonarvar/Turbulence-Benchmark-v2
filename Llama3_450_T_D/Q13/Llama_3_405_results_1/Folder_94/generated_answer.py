def find_second_largest_num(num_list):
    if len(num_list) < 41:
        return None
    selected_nums = num_list[28:41]
    if len(selected_nums) < 2:
        return None
    largest = second_largest = float('-inf')
    for num in selected_nums:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num
    if second_largest == float('-inf'):
        return None
    return second_largest