def all_left_truncatable_prime(x):
    x = x[69]
    primes = [i for i in range(2, x) if is_prime(i)]
    left_truncatable_primes = []
    for prime in primes:
        if is_left_truncatable_prime(prime):
            left_truncatable_primes.append(prime)
    return sorted(left_truncatable_primes, reverse=True)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n):
    if str(n).find('0') != -1:
        return False
    if not is_prime(n):
        return False
    for i in range(1, len(str(n))):
        if not is_prime(int(str(n)[:i])):
            return False
    return True