def find_second_largest_num(num_list):
    if len(num_list) < 2:
        return None
    max_num = second_max_num = float('-inf')
    for num in num_list[0:3]:
        if num > max_num:
            second_max_num = max_num
            max_num = num
        elif max_num > num > second_max_num:
            second_max_num = num
    return second_max_num if second_max_num != float('-inf') else None