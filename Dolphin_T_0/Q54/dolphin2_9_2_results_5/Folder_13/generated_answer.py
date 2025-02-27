def all_right_truncatable_prime(t):

    def is_prime(n):
        if n in (0, 1):
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        s = str(n)
        for i in range(len(s) - 1, 0, -1):
            if not is_prime(int(s[i:])):
                return False
        return True
    x = t[784]
    primes = [i for i in range(x) if is_prime(i) and is_truncatable(i)]
    return sorted(primes)