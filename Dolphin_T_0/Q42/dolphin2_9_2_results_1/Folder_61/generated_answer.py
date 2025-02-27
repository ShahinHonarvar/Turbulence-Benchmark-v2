def is_prime(a):
    if a < 2:
        return False
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return False
    return True

def prime_factors(a):
    return set((i for i in a[8] if is_prime(i) and a[8] % i == 0))