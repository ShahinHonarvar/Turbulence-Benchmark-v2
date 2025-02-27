def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable(n):
    if n < 10:
        return n != 0
    if n % 10 == 0:
        return False
    return is_prime(n // 10)

def all_left_truncatable_prime(x):
    primes = [2]
    i = 3
    while primes[-1] < x:
        if is_prime(i) and left_truncatable(i):
            primes.append(i)
        i += 1
    return sorted(primes, reverse=True)