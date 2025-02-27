def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def trim(n):
        while n > 10:
            n = n % 10 ** (len(str(n)) - 1)
            if not is_prime(n):
                return False
        return True
    primes = [i for i in range(2, t[89] + 1) if is_prime(i) and trim(i)]
    return sorted(primes, reverse=True)