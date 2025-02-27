def all_left_right_truncatable_prime(x):

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
        if n % 10 == 0:
            return False
        m = n
        while m >= 10:
            m = m // 10
            if not is_prime(m):
                return False
            if not is_prime(n - m * int(pow(10, m.bit_length() - 1))):
                return False
        return is_prime(n)
    primes = [i for i in range(2, x + 1) if is_truncatable_prime(i)]
    primes.sort(reverse=True)
    return primes