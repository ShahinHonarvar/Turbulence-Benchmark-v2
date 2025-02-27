def all_left_right_truncatable_prime(t: tuple) -> list:

    def is_prime(n):
        if n < 2 or n % 2 == 0:
            return False
        for j in range(3, int(n ** 0.5) + 1, 2):
            if n % j == 0:
                return False
        return True

    def truncate(n):
        while len(str(n)) > 1:
            n = int(str(n)[1:])
            if not is_prime(n):
                return False
        return True
    x = t[43]
    primes = []
    for i in range(2, x + 1):
        if is_prime(i) and (not str(i).startswith('0')) and truncate(i):
            primes.append(i)
    return primes