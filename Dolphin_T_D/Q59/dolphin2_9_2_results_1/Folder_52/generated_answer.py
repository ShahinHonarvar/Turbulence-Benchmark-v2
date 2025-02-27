def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        w = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += w
            w = 6 - w
        return True

    def is_truncatable(n):
        digits = str(n)
        for i in range(len(digits) - 1, 0, -1):
            if not is_prime(int(digits[i:])):
                return False
        return True
    x = t[52]
    primes = [i for i in range(x) if is_prime(i) and is_truncatable(i)]
    return sorted(primes, reverse=True)