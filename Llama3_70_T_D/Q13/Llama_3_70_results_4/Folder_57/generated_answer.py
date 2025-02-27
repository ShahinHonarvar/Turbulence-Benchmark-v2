def find_second_largest_num(numbers):
    sub_list = numbers[27:56]
    if len(sub_list) < 2:
        return None
    else:
        max_num = second_max = float('-inf')
        for num in sub_list:
            if num > max_num:
                second_max = max_num
                max_num = num
            elif num > second_max and num < max_num:
                second_max = num
        if second_max == float('-inf'):
            return None
        else:
            return second_max