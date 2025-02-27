def sum_in_range(lst):
    sum_range = 0
    for i in lst:
        if -3 <= i <= 6:
            sum_range += i
    return sum_range