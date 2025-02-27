def all_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        s = str(n)
        return all((is_prime(int(s[:-i])) for i in range(1, len(s))))
    x = t[26]
    primes = [i for i in range(x) if is_truncatable(i) and is_prime(i)]
    return sorted(primes)