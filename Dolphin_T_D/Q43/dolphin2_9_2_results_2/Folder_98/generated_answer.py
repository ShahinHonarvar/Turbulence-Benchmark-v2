def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    p = 3
    while p * p <= n:
        if n % p == 0:
            return False
        p += 2
    return True

def find_primes_between_indices(lst):
    primes = [x for x in lst[1:3] if is_prime(x)]
    return sorted(primes, reverse=True)