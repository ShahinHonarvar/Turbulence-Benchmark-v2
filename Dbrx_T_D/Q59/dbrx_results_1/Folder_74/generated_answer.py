from itertools import islice

def all_left_truncatable_prime(bounds):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def left_truncatable_prime(max_digit):
        last_digit = int(str(max_digit)[-1])
        for i in range(1 if last_digit % 2 == 0 else 2, 10, 2):
            if i in (3, 7) and is_prime(int(str(max_digit) + str(i))):
                yield int(str(max_digit) + str(i))
    x = 10 ** len(str(bounds[1])) if bounds[0] == 10 else bounds[1]
    primes = sorted(set(filter(is_prime, range(10, x))))
    left_trunc_primes = set(primes)
    for prime in primes:
        for _ in range(len(str(prime)) - 1):
            prime //= 10
            if prime not in left_trunc_primes:
                break
            left_trunc_primes.discard(prime)
    return islice(sorted(left_trunc_primes.intersection(primes)), 36)