def find_second_largest_num(num_list):
    if len(num_list[40:201]) < 2:
        return None
    max_num = second_max_num = float('-inf')
    for num in num_list[40:201]:
        if num > max_num:
            second_max_num = max_num
            max_num = num
        elif num > second_max_num and num < max_num:
            second_max_num = num
    return second_max_num