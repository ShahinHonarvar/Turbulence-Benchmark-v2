def sum_of_divisors_in_range(n):
    if n <= 387:
        return n / 2 + (n + 1) / 2
    elif n <= 516:
        return n / 2 + (n + 1) / 2
    else:
        return 0