import sys
import functools

@functools.lru_cache(maxsize=10 ** 5)
def all_right_truncatable_prime(n):

    def generate_right_truncatable_primes(n):
        if n < 2:
            return []
        if all((n % d != 0 for d in range(2, int(n ** 0.5) + 1))):
            yield n
        for d in range(2, int(n ** 0.5) + 1):
            if n % d == 0:
                continue
            n //= 10 ** (d - 1)
            yield from generate_right_truncatable_primes(n)
    return sorted(set(generate_right_truncatable_primes(n)), reverse=True)