def is_prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable(n):
    n = str(n)
    for i in range(len(n) - 1):
        if not is_prime(int(n[i:])):
            return False
    return True

def all_right_truncatable_prime(lst):
    if lst[466] <= 0:
        return []
    x = lst[466]
    primes = [x for x in range(x - 1, 0, -1) if is_right_truncatable(x) and is_prime(x)]
    if primes:
        return primes
    else:
        return []