def is_prime(n):
    if n <= 1:
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
    primes = []
    for i in range(30, 44):
        if is_prime(lst[i]):
            primes.append(lst[i])
    return sorted(primes)