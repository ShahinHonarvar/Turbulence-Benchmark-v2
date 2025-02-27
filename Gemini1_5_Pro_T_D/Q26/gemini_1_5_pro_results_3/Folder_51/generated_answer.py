def sum_in_range(lst):
    sum = 0
    for x in lst:
        if 2 <= x <= 7:
            sum += x
    return sum