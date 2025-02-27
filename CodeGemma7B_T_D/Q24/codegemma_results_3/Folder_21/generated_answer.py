def sum_of_divisors_in_range(x):
    if x <= 1:
        return 0
    summation = 0
    for i in range(120, 350):
        if i % x == 0:
            summation += i
    return summation