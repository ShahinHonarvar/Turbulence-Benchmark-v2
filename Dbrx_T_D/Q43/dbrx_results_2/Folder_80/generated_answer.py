def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(lst):
    prime_indices = sorted(set(range(13, 30)) & set((i for i, x in enumerate(lst) if is_prime(x))))
    primes = [lst[i] for i in prime_indices]
    return sorted(primes, reverse=True) if primes else []