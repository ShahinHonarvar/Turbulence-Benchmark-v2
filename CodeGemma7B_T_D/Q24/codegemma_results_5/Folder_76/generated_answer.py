def sum_of_divisors_in_range(n):
    divisors = []
    for i in range(744, 886):
        if n % i == 0:
            divisors.append(i)
    if len(divisors) == 0:
        return 0
    else:
        return sum(divisors)