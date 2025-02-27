def sum_of_divisors_in_range(x):
    sum = 0
    for y in range(38, 66):
        if y % x == 0:
            sum += y
    return sum