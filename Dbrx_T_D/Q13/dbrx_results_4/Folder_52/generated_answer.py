def find_second_largest_num(num_list):
    if len(num_list) < 2:
        return None
    min_num1 = max(num_list[28:38])
    min_num2 = None
    for num in num_list[28:38]:
        if num < min_num1 and (min_num2 is None or num > min_num2):
            min_num2 = num
    return min_num2