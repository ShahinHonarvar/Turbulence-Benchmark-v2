def sum_of_divisors_in_range(n):
    total = 0
    for x in range(46, 66):
        if n % x == 0:
            total += x
    return total