def sum_of_divisors_in_range(num):
    total = 0
    for i in range(46, 66):
        if num % i == 0:
            total += i
    return total if total != 0 else 0