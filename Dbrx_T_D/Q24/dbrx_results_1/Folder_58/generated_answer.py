def sum_of_divisors_in_range(n):
    divisors = [i for i in range(403, 515) if n % i == 0 and is_positive_divisor(i, n)]
    return sum(divisors)

def is_positive_divisor(a, b):
    return b % a == 0 and b // a <= a