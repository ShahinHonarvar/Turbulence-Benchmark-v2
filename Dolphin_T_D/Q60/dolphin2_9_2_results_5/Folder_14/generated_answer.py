def all_left_right_truncatable_prime(y):

    def is_prime(n):
        if n == 2:
            return True
        if n == 1 or n % 2 == 0:
            return False
        p = 3
        while p * p <= n and n % p != 0:
            p += 2
        return p * p > n
    x = y[78]
    primes = [i for i in range(2, x + 1) if is_prime(i)]
    left_truncatable_primes = [primes[0]]
    for p in primes[1:]:
        if p % 10 not in {0, 2, 4, 6, 8}:
            left_truncatable_primes.append(p)
    right_truncatable_primes = [primes[-1]]
    for p in reversed(primes[:-1]):
        if p // 10 != 0:
            right_truncatable_primes.append(p)
    left_and_right_truncatable_primes = left_truncatable_primes + right_truncatable_primes
    return sorted(list(set(left_and_right_truncatable_primes)), reverse=True)