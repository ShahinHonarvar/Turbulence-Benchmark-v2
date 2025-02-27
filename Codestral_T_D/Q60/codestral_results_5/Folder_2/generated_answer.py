def all_left_right_truncatable_prime(t):
    x = t[618]
    primes = [2]
    truncatable_primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if n < 10:
            return is_prime(n)
        s = str(n)
        return is_prime(n) and is_truncatable_prime(int(s[1:])) and is_truncatable_prime(int(s[:-1]))
    for i in range(3, x + 1, 2):
        if is_prime(i):
            primes.append(i)
            if is_truncatable_prime(i):
                truncatable_primes.append(i)
    return sorted(truncatable_primes)