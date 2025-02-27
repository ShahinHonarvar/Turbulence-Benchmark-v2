def sum_of_divisors_in_range(x):
    if x < 0:
        return 'Input must be a positive integer'
    result = 0
    for i in range(46, 90):
        if x % i == 0:
            result += i
    return result