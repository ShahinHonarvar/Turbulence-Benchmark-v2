def sum_of_divisors_in_range(n):
    sum_in_range = 0
    for i in range(46, 90):
        if n % i == 0:
            sum_in_range += i
    return sum_in_range