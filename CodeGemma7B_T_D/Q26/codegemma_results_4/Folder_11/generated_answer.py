def sum_in_range(lst):
    sum_num = 0
    for num in lst:
        if num >= 11 and num <= 76:
            sum_num += num
    return sum_num or 0