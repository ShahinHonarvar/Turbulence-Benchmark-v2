def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n):
    if '0' in str(n):
        return False
    for i in range(1, len(str(n))):
        if not is_prime(int(str(n)[:i])):
            return False
    return True

def all_left_truncatable_prime(tup):
    x = tup[39]
    primes = []
    for n in range(x - 1, 0, -1):
        if is_left_truncatable_prime(n):
            primes.append(n)
    return sorted(primes, reverse=True)