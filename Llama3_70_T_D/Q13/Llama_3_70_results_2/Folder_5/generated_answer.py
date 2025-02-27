def find_second_largest_num(num_list):
    num_list = num_list[8:10]
    if len(num_list) < 2:
        return None
    max_num = second_max = float('-inf')
    for num in num_list:
        if num > max_num:
            second_max = max_num
            max_num = num
        elif num > second_max and num < max_num:
            second_max = num
    return second_max