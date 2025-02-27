def find_second_largest_num(numbers):
    sub_list = numbers[59:98]
    if len(sub_list) < 2:
        return None
    max_num = second_max_num = float('-inf')
    for num in sub_list:
        if num > max_num:
            second_max_num = max_num
            max_num = num
        elif second_max_num < num < max_num:
            second_max_num = num
    return None if second_max_num == float('-inf') else second_max_num