def is_prime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(lst):
    primes = [i for i in lst[57:65] if is_prime(i)]
    if not primes:
        return []
    return sorted(primes, reverse=True)