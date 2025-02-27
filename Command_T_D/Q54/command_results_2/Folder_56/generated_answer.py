import itertools

def all_right_truncatable_prime(n):
    primes = [x for x in range(2, n) if all((x % d != 0 for d in range(3, int(x ** 0.5) + 1, 2)))]
    right_truncatable_primes = []
    for p in primes:
        if p % 10:
            for d in range(1, 10):
                if p % d == 0:
                    break
                elif d == 10:
                    break
                elif p // d * d == p:
                    right_truncatable_primes.append(p)
                    break
    return sorted(right_truncatable_primes)