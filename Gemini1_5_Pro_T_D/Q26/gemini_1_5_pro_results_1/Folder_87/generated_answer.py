def sum_in_range(lst):
    sum = 0
    for x in lst:
        if x >= 60 and x <= 90:
            sum += x
    return sum