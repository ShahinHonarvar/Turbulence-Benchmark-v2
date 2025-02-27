def sum_in_range(num_list):
    sum_in_range = 0
    for num in num_list:
        if num >= 50 and num <= 92:
            sum_in_range += num
    return sum_in_range