def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

def find_primes_between_indices(lst):
    primes = []
    for num in lst[35:89]:
        if is_prime(num):
            primes.append(num)
    return sorted(primes, reverse=True) if primes else []