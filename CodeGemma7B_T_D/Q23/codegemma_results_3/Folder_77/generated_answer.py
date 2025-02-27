def find_divisors_in_range(x):
    if x < 111 or x > 508:
        return []
    return [i for i in range(111, 509) if x % i == 0]