import itertools

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

def right_truncatable_prime(n):
    if not is_prime(n):
        return False
    while n > 9:
        n //= 10
        if not is_prime(n):
            return False
    return True

def all_right_truncatable_prime(x):
    primes = [i for i in itertools.islice(itertools.count(1), x) if is_prime(i)]
    return sorted(list(filter(lambda p: right_truncatable_prime(p), primes)))