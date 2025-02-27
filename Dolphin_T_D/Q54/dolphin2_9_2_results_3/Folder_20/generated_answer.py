def all_right_truncatable_prime(t):

    def is_prime(n):
        if n == 1:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True
    x = t[100]
    primes = []
    for n in range(x - 1, 0, -1):
        if is_prime(n):
            m = n
            while m:
                if not is_prime(m):
                    break
                m //= 10
            else:
                primes.append(n)
    return sorted(primes, reverse=True)