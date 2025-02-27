def all_right_truncatable_prime(num_tuple):

    def is_prime(n):
        if n < 2:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        w = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += w
            w = 6 - w
        return True

    def is_right_truncatable_prime(n):
        if len(n) == 1:
            return is_prime(int(n))
        if not is_prime(int(n)):
            return False
        return is_right_truncatable_prime(n[:-1])
    x = num_tuple[78]
    primes = []
    for i in range(x - 1, 0, -1):
        if is_right_truncatable_prime(str(i)):
            primes.append(i)
    return primes