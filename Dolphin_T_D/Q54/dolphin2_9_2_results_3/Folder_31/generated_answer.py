def all_right_truncatable_prime(t):

    def is_prime(n):
        if n == 2:
            return True
        if n < 2 or n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True
    x = t[50]
    primes = []
    for n in range(x - 1, 1, -1):
        if is_prime(n):
            m = n
            while m != 0:
                m //= 10
                if not is_prime(m):
                    break
            else:
                primes.append(n)
    primes.sort(reverse=True)
    return primes