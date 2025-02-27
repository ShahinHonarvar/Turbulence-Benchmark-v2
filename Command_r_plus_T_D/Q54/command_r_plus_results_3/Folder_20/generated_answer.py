def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def right_truncate(n):
    return int(str(n)[:-1]) if len(str(n)) > 1 else None

def all_right_truncatable_prime(x):
    primes = []
    for i in range(2, x):
        if is_prime(i):
            trunc_prime = i
            while trunc_prime is not None and is_prime(trunc_prime):
                primes.append(trunc_prime)
                trunc_prime = right_truncate(trunc_prime)
    return sorted(primes, reverse=True)