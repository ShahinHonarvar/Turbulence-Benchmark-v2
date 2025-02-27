def find_divisors_in_range(n):
    divisors = [i for i in range(10, 56) if n % i == 0 and i > 0]
    return divisors