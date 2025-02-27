def sum_in_range(lst):
    sum_range = 0
    for num in lst:
        if num >= 3 and num <= 8:
            sum_range += num
    return sum_range or 0