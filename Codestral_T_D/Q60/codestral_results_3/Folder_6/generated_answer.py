def all_left_right_truncatable_prime(num_tuple):
    x = num_tuple[74]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        while n > 0:
            if n % 10 == 0:
                return False
            if not is_prime(n):
                return False
            n //= 10
        return True

    def is_right_truncatable(n):
        s = str(n)
        while len(s) > 0:
            if not is_prime(int(s)):
                return False
            s = s[:-1]
        return True
    lr_truncatable_primes = []
    for i in range(2, x + 1):
        if is_left_truncatable(i) and is_right_truncatable(i):
            lr_truncatable_primes.append(i)
    return sorted(lr_truncatable_primes)