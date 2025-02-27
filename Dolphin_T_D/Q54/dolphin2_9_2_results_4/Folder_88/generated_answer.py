def all_right_truncatable_prime(lst):
    x = lst[93]
    primes = [2, 3, 5, 7]
    for p in primes:
        if is_truncatable(p, x):
            primes.append(p)
    return sorted(primes)

def is_truncatable(n, x):
    if n > x:
        return False
    if is_prime(n):
        return True
    return False

def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True