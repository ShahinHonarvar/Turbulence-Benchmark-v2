def find_divisors_in_range(n):
    divisors = [i for i in range(6, 10) if n % i == 0]
    return divisors