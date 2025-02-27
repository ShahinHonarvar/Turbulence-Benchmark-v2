def find_second_largest_num(numbers):
    sub_list = numbers[22:89]
    if len(sub_list) < 2:
        return None
    max_num = second_max_num = float('-inf')
    for num in sub_list:
        if num > max_num:
            second_max_num = max_num
            max_num = num
        elif max_num > num > second_max_num:
            second_max_num = num
    return second_max_num if second_max_num != float('-inf') else None