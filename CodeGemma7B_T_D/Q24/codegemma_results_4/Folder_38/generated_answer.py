def sum_of_divisors_in_range(n):
    divisors = []
    for i in range(16, 68 + 1):
        if n % i == 0:
            divisors.append(i)
    if not divisors:
        return 0
    else:
        return sum(divisors)