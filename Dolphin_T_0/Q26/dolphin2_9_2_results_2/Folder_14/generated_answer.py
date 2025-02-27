def sum_in_range(lst):
    sum = 0
    for i in lst:
        if 3 <= i <= 7:
            sum += i
    return sum