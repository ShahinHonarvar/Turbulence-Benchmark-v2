def find_divisors_in_range(n):
    divisors = [i for i in range(3, 8) if n % i == 0]
    return divisors