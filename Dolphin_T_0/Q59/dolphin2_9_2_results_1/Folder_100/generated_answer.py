def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, se(int(n ** 0.5) + 1)):
            if n % i == 0:
                return False
        return True

    def is_truncatable(p):
        if '0' in str(p):
            return False
        i = str(p)
        while len(i) > 0:
            if not is_prime(int(i)):
                return False
            i = i[1:]
        return True
    x = t[26]
    left_truncatable_primes = [p for p in range(2, x) if is_truncatable(p)]
    return sorted(left_truncatable_primes)