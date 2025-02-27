import itertools

def all_right_truncatable_prime(n):
    primes = set(itertools.chain.from_iterable((str(n) for n in range(2, int(str(n) + '0') + 1) if all((n % d == 0 for d in range(2, int(str(n) + '0') + 1))))))
    return [int(p) for p in primes if all((p % d == 0 for d in range(2, int(str(p) + '0') + 1)))]