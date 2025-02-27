def all_left_truncatable_prime(x_tuple):

    def is_prime(n):
        if n in (2, 3):
            return True
        if n % 2 == 0 or n == 1:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    def is_left_truncatable_prime(n):
        if n in (2, 3):
            return True
        for i in range(2, len(str(n))):
            if not is_prime(int(str(n)[i:])):
                return False
        return True
    x = x_tuple[79]
    primes = []
    for i in range(x - 1, 1, -1):
        if is_prime(i) and is_left_truncatable_prime(i):
            primes.append(i)
    return primes