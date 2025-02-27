def sum_in_range(num_list):
    result = 0
    for num in num_list:
        if num >= 1 and num <= 7:
            result += num
    return result