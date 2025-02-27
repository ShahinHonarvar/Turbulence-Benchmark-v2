import itertools

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

def left_truncatable_primes():
    yield 2
    for length in itertools.count(1):
        for num in map(int, itertools.product('123456789', repeat=length)):
            if num % 100 == 0:
                continue
            if is_prime(num):
                yield num

def all_left_truncatable_prime(x):
    primes = list(itertools.islice(left_truncatable_primes(), 96))
    return sorted([p for p in primes if p < x], reverse=True)