def is_prime(n):
    if n == 0 or n == 1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

def find_primes_between_indices(lst):
    primes = []
    for i in range(24, 33):
        if is_prime(lst[i]):
            primes.append(lst[i])
    primes.sort(reverse=True)
    return primes if primes else []