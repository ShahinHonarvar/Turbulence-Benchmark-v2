def find_divisors_in_range(num):
    divisors = [d for d in range(2, 7) if num % d == 0]
    return divisors