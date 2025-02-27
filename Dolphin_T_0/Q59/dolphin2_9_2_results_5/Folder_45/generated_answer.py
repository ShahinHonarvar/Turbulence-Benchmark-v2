def all_left_truncatable_prime(t):
    x = t[61]

    def is_prime(n):
        if n != 1 and n != 0:
            for i in range(2, n):
                if n % i == 0:
                    return False
        return True

    def is_truncatable(n):
        num = n
        while num > 0:
            if not is_prime(num):
                return False
            num = num // 10
        return True
    primes = [i for i in range(2, x) if is_prime(i)]
    truncatable = [i for i in primes if is_truncatable(i)]
    return sorted(truncatable)