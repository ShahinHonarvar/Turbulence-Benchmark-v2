def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(indices):
    primes = [num for num in indices[36:41] if is_prime(num)]
    return sorted(primes, reverse=True) if primes else []