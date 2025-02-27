def sum_in_range(list):
    sum_range = 0
    for num in list:
        if num >= 32 and num <= 44:
            sum_range += num
    return sum_range