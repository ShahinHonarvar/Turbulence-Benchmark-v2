def all_right_truncatable_prime(int_tuple):

    def is_prime(n):
        if n < 2 or (n % 2 == 0 and n > 2):
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        while n > 0 and is_prime(n):
            n //= 10
        return n == 0

    def right_truncatable_prime(n):
        primes = []
        if is_right_truncatalog(n):
            return True
        else:
            if is_prime(n):
                primes.append(n)
            for i in range(1, len(str(n))):
                if is_prime(n // 10 ** i):
                    primes.append(n // 10 ** i)
        return primes
    x = int_tuple[79]
    right_truncatable_primes = []
    for i in range(x, 0, -1):
        if is_prime(i):
            if len(right_truncatable_prime(i)) > 0:
                right_truncatable_primes.extend(right_truncatable_prime(i))
    if len(right_truncatable_primes) > 0:
        return sorted(right_truncatable_primes, reverse=True)
    else:
        return []