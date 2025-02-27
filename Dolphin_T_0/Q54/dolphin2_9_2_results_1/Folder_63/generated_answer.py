def all_right_truncatable_prime(t):

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0:
            return False
        sqr = int(n ** 0.5) + 1
        for divisor in range(3, sqr, 2):
            if n % divisor == 0:
                return False
        return True
    x = t[88]
    primes = []
    for n in range(2, x):
        if is_prime(n):
            n_str = str(n)
            for _ in range(1, n_str.__len__()):
                if not is_prime(int(n_str[1:])):
                    break
                n_str = n_str[1:]
            else:
                primes.append(n)
    return primes