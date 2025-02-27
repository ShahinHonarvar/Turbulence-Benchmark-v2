def all_left_truncatable_prime(tup):

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(num):
        while num:
            if not is_prime(num):
                return False
            num //= 10
        return True
    x = tup[73]
    primes = []
    for i in range(x - 1, 1, -1):
        if i % 10 == 0 or not is_prime(i):
            continue
        if is_left_truncatable(i):
            primes.append(i)
    return primes