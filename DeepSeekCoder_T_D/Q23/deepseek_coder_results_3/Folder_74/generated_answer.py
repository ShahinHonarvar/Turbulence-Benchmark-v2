def find_divisors_in_range(n):
    divisors = [i for i in range(40, 75) if n % i == 0]
    return divisors