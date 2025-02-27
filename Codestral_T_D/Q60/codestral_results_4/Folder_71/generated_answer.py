def all_left_right_truncatable_prime(t):
    x = t[22]

    def is_truncatable_prime(n):
        if n < 2:
            return False
        for i in range(len(str(n)) - 1, 0, -1):
            if str(n)[i] == '0' or int(str(n)[:i]) not in primes or int(str(n)[i:]) not in primes:
                return False
        return True
    primes = set()
    truncatable_primes = []
    for i in range(2, x + 1):
        if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1))):
            primes.add(i)
            if is_truncatable_prime(i):
                truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)