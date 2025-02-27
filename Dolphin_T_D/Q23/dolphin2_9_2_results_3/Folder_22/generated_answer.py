def find_divisors_in_range(x):
    divisors = [i for i in range(4, 8) if x % i == 0]
    if not divisors:
        return []
    return divisors