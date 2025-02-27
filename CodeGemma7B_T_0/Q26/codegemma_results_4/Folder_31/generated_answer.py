def sum_in_range(num_list):
    sum = 0
    for num in num_list:
        if num >= 60 and num <= 97:
            sum += num
    return sum