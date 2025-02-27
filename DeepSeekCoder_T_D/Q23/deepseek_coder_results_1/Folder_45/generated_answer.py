def find_divisors_in_range(n):
    divisors = [i for i in range(4, 9) if n % i == 0]
    return divisors