def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_sieve(limit):
    primes = set()
    for i in range(2, limit + 1):
        if is_prime(i):
            primes.add(i)
    return primes

def all_left_right_truncatable_prime(tup):
    str_tup = ''.join((str(num) for num in tup))
    x = int(str_tup[370])
    truncatable_primes = set()
    for prime in prime_sieve(x):
        if '0' not in str(prime):
            for i in range(len(str(prime)) - 1):
                truncatable_prime = int(str(prime)[:-i - 1:-1])
                if not is_prime(truncatable_prime):
                    break
            else:
                truncatable_primes.add(prime)
    return sorted(list(truncatable_primes), reverse=True)