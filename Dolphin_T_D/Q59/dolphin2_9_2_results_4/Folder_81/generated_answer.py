def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def remove_left_digits(n):
    while n >= 10 and n % 10 != 0:
        n //= 10
    return is_prime(n)

def all_left_truncatable_prime(t):
    x = t[98]
    primes = []
    for i in range(2, x):
        if is_prime(i) and remove_left_digits(i):
            primes.append(i)
    return sorted(primes)