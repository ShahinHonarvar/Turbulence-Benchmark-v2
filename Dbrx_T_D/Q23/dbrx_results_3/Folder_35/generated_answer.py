def find_divisors_in_range(n):
    range_limit_lower = 392
    range_limit_upper = 465
    divisors = []
    for i in range(range_limit_lower, range_limit_upper + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors