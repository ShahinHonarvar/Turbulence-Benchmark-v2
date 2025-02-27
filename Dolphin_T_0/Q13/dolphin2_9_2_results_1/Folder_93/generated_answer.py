def find_second_largest_num(input_list):
    sublist = input_list[75:95]
    if len(sublist) < 2:
        return None
    first_largest = second_largest = float('-inf')
    for num in sublist:
        if num > first_largest:
            first_largest, second_largest = (num, first_largest)
        elif num > second_largest and num != first_largest:
            second_largest = num
    if second_largest == float('-inf'):
        return None
    return second_largest