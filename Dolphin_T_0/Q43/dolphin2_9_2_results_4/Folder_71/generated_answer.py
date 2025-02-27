def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def find_primes_between_indices(lst):
    primes = [num for num in lst[57:65] if is_prime(num)]
    return sorted(primes, reverse=True) if primes else []