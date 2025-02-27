def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False
    sqrt_n = int(n ** 0.5) + 1
    for i in range(3, sqrt_n, 2):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(lst):
    primes = [num for num in lst[478:950] if is_prime(num)]
    return sorted(primes, reverse=True) if primes else []