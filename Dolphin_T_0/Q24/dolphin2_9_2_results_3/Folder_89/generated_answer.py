def sum_of_divisors_in_range(n):
    result = 0
    for d in range(14, 49):
        if n > 0 and n % d == 0:
            result += d
    return result