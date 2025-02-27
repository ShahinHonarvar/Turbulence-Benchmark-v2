def sum_of_divisors_in_range(n):
    divisors = []
    for i in range(38, 66):
        if n % i == 0:
            divisors.append(i)
    if len(divisors) == 0:
        return 0
    else:
        return sum(divisors)