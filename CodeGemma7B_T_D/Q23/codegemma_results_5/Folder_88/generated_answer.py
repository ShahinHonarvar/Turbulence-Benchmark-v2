def find_divisors_in_range(x):
    if x <= 0:
        return []
    return [i for i in range(6, x + 1) if x % i == 0]