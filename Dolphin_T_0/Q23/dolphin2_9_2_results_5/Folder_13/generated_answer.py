def find_divisors_in_range(n):
    lower_bound = 472
    upper_bound = 827
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            lower_divisor = n // i
            upper_divisor = n // lower_divisor
            if lower_divisor >= lower_bound and lower_divisor <= upper_bound:
                divisors.append(lower_divisor)
            if upper_divisor >= lower_bound and upper_divisor <= upper_bound:
                divisors.append(upper_divisor)
    return divisors