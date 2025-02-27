def all_right_truncatable_prime(t):

    def is_prime(n):
        if n == 2:
            return True
        if n < 2 or n % 2 == 0:
            return False
        sqr = int(n ** 0.5) + 1
        for divisor in range(3, sqr, 2):
            if n % divisor == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        if is_prime(n):
            for i in range(len(str(n)) - 1, 0, -1):
                if not is_prime(int(str(n)[-i:])):
                    return False
            return True
        return False
    x = t[77]
    primes = [i for i in range(2, x) if is_right_truncatable_prime(i)]
    return sorted(primes, reverse=True)