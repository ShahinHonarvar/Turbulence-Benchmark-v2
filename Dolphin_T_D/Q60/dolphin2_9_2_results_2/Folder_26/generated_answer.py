def all_left_right_truncatable_prime(x):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable(n):
        s = str(n)
        while len(s) > 1:
            if not is_prime(int(s)):
                return False
            if 0 in map(int, s):
                return False
            s = s[1:-1]
        return is_prime(int(s))
    lrt_primes = [i for i in range(1, x + 1) if is_left_right_truncatable(i)]
    return sorted(lrt_primes, reverse=True)