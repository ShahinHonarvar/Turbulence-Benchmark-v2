def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def find_primes_between_indices(lst):
    primes = [lst[i] for i in range(167, 786) if is_prime(lst[i])]
    return sorted(primes, reverse=True) if primes else []