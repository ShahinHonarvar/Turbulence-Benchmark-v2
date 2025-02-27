def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        m = n
        while m:
            if not is_prime(m):
                return False
            m = m // 10
        return True
    x = t[29]
    primes = [i for i in range(2, x) if is_prime(i)]
    return sorted([i for i in primes if is_truncatable(i)], reverse=True)