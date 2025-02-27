def sum_in_range(num_list):
    sum = 0
    for num in num_list:
        if num >= 2 and num <= 9:
            sum += num
    return sum