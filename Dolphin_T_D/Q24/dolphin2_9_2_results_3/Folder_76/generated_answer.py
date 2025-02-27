def sum_of_divisors_in_range(n):
    sum_of_divisors = 0
    for i in range(744, 886):
        if n % i == 0:
            sum_of_divisors += i
    if sum_of_divisors > 0:
        return sum_of_divisors
    else:
        return 0