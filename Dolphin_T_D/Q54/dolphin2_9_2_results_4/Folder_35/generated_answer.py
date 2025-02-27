def all_right_truncatable_prime(x):

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

    def is_right_truncatable_prime(p):
        str_p = str(p)
        for i in range(len(str_p) - 1, 0, -1):
            if not is_prime(int(str_p[i:])):
                return False
        return True
    primes = [2]
    for i in range(3, x):
        if is_prime(i):
            primes.append(i)
    right_truncatable_primes = [p for p in primes if is_right_truncatable_prime(p)]
    return right_truncatable_primes