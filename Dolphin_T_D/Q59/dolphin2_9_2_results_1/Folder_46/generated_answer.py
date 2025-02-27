def all_left_truncatable_prime(x):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(p):
        if p == 0 or not is_prime(p):
            return False
        while p:
            if not is_prime(p):
                return False
            p //= 10
        return True
    primes = [2]
    if x <= 2:
        return primes
    i = 3
    while i < x:
        if is_prime(i):
            if is_left_truncatable_prime(i):
                primes.append(i)
            i += 2
        else:
            i += 1
    return primes