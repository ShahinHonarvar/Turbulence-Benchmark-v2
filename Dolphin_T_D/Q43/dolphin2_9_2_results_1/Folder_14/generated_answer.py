def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i:
            i += 2
        else:
            return False
    return True

def find_primes_between_indices(num_list):
    primes = [n for n in num_list[10:67] if is_prime(n)]
    return sorted(primes) if primes else []