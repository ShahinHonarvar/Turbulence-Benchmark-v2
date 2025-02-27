def all_right_truncatable_prime(num_tuple):

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

    def is_right_truncatable(n):
        if len(str(n)) == 1:
            return is_prime(n)
        return is_prime(n) and is_right_truncatable(n // 10)
    x = num_tuple[630]
    primes = []
    for i in range(2, x):
        if is_right_truncatable(i):
            primes.append(i)
    return sorted(primes, reverse=True)