def all_right_truncatable_prime(t):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    x = t[93]
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
    return sorted(primes)