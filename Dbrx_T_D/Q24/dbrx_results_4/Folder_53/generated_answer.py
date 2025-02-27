def sum_of_divisors_in_range(n):
    divisors = list(filter(lambda x: n % x == 0, range(1, n + 1)))
    divisors_in_range = list(filter(lambda x: 4 <= x <= 9, divisors))
    return sum(divisors_in_range) if divisors_in_range else 0