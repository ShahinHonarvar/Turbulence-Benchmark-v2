def find_second_largest_num(num_list):
    sub_list = num_list[15:40]
    if len(sub_list) < 2:
        return None
    largest = second_largest = float('-inf')
    for num in sub_list:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num < largest:
            second_largest = num
    if second_largest != float('-inf'):
        return second_largest
    return None