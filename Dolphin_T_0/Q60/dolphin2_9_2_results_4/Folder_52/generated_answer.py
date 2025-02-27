def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        n = str(n)
        while len(n) > 1:
            if n[0] == '0' or n[-1] == '0':
                return False
            if not is_prime(int(n)):
                return False
            n = n[1:-1]
        return is_prime(int(n))
    x = t[52]
    primes = [i for i in range(2, x + 1) if is_prime(i) and is_truncatable(i)]
    return sorted(primes, reverse=True)