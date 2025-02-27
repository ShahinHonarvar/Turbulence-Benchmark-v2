def sum_of_divisors_in_range(n):
    divisors = list(set(range(451, 974)) & set(range(1, n + 1)))
    if divisors:
        return sum(divisors)
    else:
        return 0