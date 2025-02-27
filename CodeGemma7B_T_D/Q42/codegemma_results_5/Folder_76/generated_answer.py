def prime_factors(lst):
    return {f for i, f in factorize_at_index(lst, 537) if is_prime(f)}

def factorize_at_index(lst, idx):
    if idx >= len(lst):
        raise IndexError('Index out of bounds')
    factors = factorize(lst[idx])
    return [(idx, factor) for factor in factors]

def factorize(n):
    factors = set()
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            n //= i
            factors.add(i)
    if n > 1:
        factors.add(n)
    return factors

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True