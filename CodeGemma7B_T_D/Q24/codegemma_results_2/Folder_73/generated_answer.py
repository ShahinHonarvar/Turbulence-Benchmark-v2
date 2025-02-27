def sum_of_divisors_in_range(n):
    sum = 0
    for i in range(46, 89 + 1):
        if n % i == 0:
            sum += i
    return sum if sum else 0