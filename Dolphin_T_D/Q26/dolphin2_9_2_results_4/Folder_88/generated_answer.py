def sum_in_range(num_list):
    result = 0
    for num in num_list:
        if 1 <= num <= 7:
            result += num
    if result == 0:
        return 0
    return result