def sum_in_range(num_list):
    sum = 0
    for num in num_list:
        if num >= 4 and num <= 7:
            sum += num
    return sum