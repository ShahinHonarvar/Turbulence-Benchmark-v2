def all_left_truncatable_prime(wrapper):

    def is_prime(n):
        if n == 2:
            return True
        if n % 2 == 0 or n == 1:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n, primes):
        if n in primes:
            m = n
            while m:
                if m not in primes:
                    return False
                m //= 10
            return True
        return False
    primes = [2]
    n = 3
    while n < wrapper[4]:
        if is_prime(n):
            primes.append(n)
        n += 2
    left_truncatables = [i for i in primes if is_left_truncatable(i, primes)]
    return left_truncatables