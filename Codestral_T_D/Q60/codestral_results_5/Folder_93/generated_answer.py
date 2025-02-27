def all_left_right_truncatable_prime(t):

    def is_truncatable_prime(n):
        if n < 2 or '0' in str(n):
            return False
        primes = [2]
        for i in range(3, int(n ** 0.5) + 1, 2):
            if all((i % p != 0 for p in primes)):
                primes.append(i)
        for p in primes:
            if n % p == 0:
                return False
        s = str(n)
        return all((is_truncatable_prime(int(s[i:])) and is_truncatable_prime(int(s[:-i])) for i in range(1, len(s))))
    x = t[11]
    return sorted([n for n in range(2, x + 1) if is_truncatable_prime(n)])