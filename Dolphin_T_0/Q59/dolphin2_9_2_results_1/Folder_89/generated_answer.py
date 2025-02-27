def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[97]
    primes = []
    for n in range(x - 1, 1, -1):
        if is_prime(n):
            m = n
            while m:
                if not is_prime(m):
                    break
                m //= 10
            else:
                primes.append(n)
    return primes