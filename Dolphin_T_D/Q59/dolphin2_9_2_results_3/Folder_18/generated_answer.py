def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatables(n):
    if n < 10:
        return [n]
    else:
        return [n] + left_truncatables(n // 10)

def all_left_truncatable_prime(t):
    x = t[429]
    primes = [i for i in range(2, x) if is_prime(i)]
    truncatable_primes = []
    for prime in primes:
        if set(map(is_prime, left_truncatables(prime))) == {True}:
            truncatable_primes.append(prime)
    return sorted(truncatable_primes, reverse=True)