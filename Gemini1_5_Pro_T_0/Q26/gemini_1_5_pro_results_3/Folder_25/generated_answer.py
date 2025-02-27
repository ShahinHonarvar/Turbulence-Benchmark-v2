def sum_in_range(lst):
    sum = 0
    for x in lst:
        if -10 <= x <= 48:
            sum += x
    return sum