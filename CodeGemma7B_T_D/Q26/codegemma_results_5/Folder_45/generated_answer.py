def sum_in_range(lst):
    sum_range = 0
    for num in lst:
        if num >= 3 and num <= 4:
            sum_range += num
    return sum_range