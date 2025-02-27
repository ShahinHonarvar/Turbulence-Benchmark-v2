def sum_of_divisors_in_range(n):
    lower_limit = 11
    upper_limit = 41
    total = 0
    for i in range(lower_limit, upper_limit + 1):
        if n % i == 0:
            total += i
    return total