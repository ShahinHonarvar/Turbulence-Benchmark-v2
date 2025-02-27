def sum_in_range(int_list):
    result = 0
    for num in int_list:
        if num >= 8 and num <= 9:
            result += num
    return result