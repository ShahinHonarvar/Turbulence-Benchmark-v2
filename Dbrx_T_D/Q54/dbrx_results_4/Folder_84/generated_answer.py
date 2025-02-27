import itertools

def generate_primes(n):
    primes = []
    sieve = [True] * (n + 1)
    for num in range(2, int(n ** 0.5) + 1):
        if sieve[num]:
            primes.append(num)
            for multiple in range(num * num, n + 1, num):
                sieve[multiple] = False
    primes.extend((i for i in range(int(n ** 0.5) + 1, n + 1) if sieve[i]))
    return primes

def is_right_truncatable_prime(n):
    while n > 0:
        if not n in primes:
            return False
        n = n // 10
    return True

def all_right_truncatable_prime(tup):
    right_truncatable_primes = []
    for num in itertools.islice(itertools.takewhile(lambda x: x < tup[0], itertools.count()), len(tup)):
        if is_right_truncatable_prime(num):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)