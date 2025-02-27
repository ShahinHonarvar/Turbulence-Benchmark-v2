def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def is_right_truncatable_prime(n):
    while n >= 10:
        n = int(str(n)[1:])
        if not is_prime(n):
            return False
    return is_prime(n)

def all_right_truncatable_prime(tup):
    x = tup[89]
    primes = []
    for i in range(1, x):
        if is_right_truncatable_prime(i):
            primes.append(i)
    return sorted(primes, reverse=True)