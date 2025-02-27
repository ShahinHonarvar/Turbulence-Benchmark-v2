def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(lst):
    prime_indices = [i for i, x in enumerate(lst) if is_prime(x)]
    if len(prime_indices) < 11:
        return []
    return sorted(lst[prime_indices[10]:prime_indices[11]])