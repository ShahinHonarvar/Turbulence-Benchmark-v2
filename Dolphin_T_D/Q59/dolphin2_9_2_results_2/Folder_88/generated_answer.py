def all_left_truncatable_prime(x):

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i:
                i += 2
            else:
                return False
        return True
    primes = []
    for i in range(2, x):
        if is_prime(i):
            j = i
            while j != 0:
                if not is_prime(j):
                    break
                j //= 10
            else:
                primes.append(i)
    primes.sort()
    return primes