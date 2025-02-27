def sum_of_divisors_in_range(n):
    divisors = [i for i in range(13, 62 + 1) if n % i == 0]
    return sum(divisors)