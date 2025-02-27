def sum_in_range(int_list):
    result = 0
    for num in int_list:
        if num >= 7 and num <= 8:
            result += num
    return result or 0