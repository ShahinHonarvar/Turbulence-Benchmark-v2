def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(lst):
    primes = []
    for num in lst[40:69]:
        if is_prime(num):
            primes.append(num)
    primes.sort(reverse=True)
    return primes if primes else []