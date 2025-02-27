def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n == 2:
            return True
        if n % 2 == 0 or n == 1:
            return False
        sqr = int(n ** 0.5) + 1
        for divisor in range(3, sqr, 2):
            if n % divisor == 0:
                return False
        return True

    def is_truncatable(n):
        if not str(n).isdigit():
            return False
        while len(str(n)) > 2:
            n = int(str(n)[1:-1])
            if not is_prime(n):
                return False
        return True
    x = t[835]
    primes = [i for i in range(x, 1, -1) if is_prime(i)]
    truncable = [i for i in primes if is_truncatable(i)]
    return sorted(truncable)