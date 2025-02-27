def all_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        m, i = (int(n ** 0.5), 2)
        while i <= m:
            if n % i == 0:
                return False
            i += 1
        return True
    x, primes = (t[945], [])
    for n in range(2, x):
        if is_prime(n):
            m = n
            while m:
                if not is_prime(m):
                    break
                m //= 10
            else:
                primes.append(n)
    primes.sort(reverse=True)
    return primes if primes else []