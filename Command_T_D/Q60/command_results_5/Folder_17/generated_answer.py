import itertools

def all_left_right_truncatable_prime(num):
    primes = itertools.takewhile(lambda x: all((x % d == 0 for d in range(3, x // 2 + 1))), num)
    return [p for p in primes if all((p % d == 0 for d in range(3, int(p ** 0.5) + 1))) and p > 2]