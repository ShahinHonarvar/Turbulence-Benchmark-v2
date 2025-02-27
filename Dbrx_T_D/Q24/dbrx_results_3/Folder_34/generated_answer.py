def sum_of_divisors_in_range(n):
    divisors = [i for i in range(4, 6) if n % i == 0 and is_positive_divisor(i, n)]
    return sum(divisors)

def is_positive_divisor(d, n):
    return n % d == 0 and d > 0