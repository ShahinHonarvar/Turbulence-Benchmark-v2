def sum_in_range(lst):
    sum = 0
    for i in lst:
        if i >= 18 and i <= 52:
            sum += i
    return sum