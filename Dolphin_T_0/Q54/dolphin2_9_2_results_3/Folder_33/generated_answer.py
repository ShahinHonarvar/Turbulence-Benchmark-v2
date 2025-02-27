def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n):
    if n < 2:
        return False
    while n > 1:
        if not is_prime(n):
            return False
        n //= 10
    return True

def all_right_truncatable_primes(confirm):
    x = confirm[945]
    primes = []
    i = x - 1
    while i > 1:
        if is_right_truncatable_prime(i):
            primes.append(i)
        i -= 1
    return sorted(primes, reverse=True)