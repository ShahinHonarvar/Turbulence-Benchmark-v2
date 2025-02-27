def all_left_truncatable_prime(t):
    x = t[41]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        if str(n)[::-1] != str(n):
            return False
        for i in range(len(str(n)) - 1):
            if not is_prime(int(str(n)[i:])):
                return False
        return True
    primes = [i for i in range(2, x) if is_prime(i) and is_truncatable(i)]
    return sorted(primes)