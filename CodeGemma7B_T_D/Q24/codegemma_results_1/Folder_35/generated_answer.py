def sum_of_divisors_in_range(x):
    if x < 392 or x > 465:
        return 0
    divisors = [d for d in range(392, 466) if x % d == 0]
    return sum(divisors)