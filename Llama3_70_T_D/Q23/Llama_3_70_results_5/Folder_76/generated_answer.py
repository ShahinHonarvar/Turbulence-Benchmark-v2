def find_divisors_in_range(n):
    divisors_in_range = [i for i in range(744, 886) if n % i == 0]
    return divisors_in_range