def find_second_smallest_num(num_list):
    if not num_list or len(num_list) < 2:
        return None
    min_num = float('inf')
    second_min_num = float('inf')
    for num in num_list:
        if num < min_num:
            min_num, second_min_num = (num, min_num)
        elif num < second_min_num and num != min_num:
            second_min_num = num
    if second_min_num == float('inf'):
        return None
    return second_min_num