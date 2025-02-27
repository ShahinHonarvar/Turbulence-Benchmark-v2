def all_right_truncatable_prime(positive_integers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = positive_integers[86]
    primes = []
    for i in range(x - 1, 1, -1):
        if is_prime(i):
            j = i
            while j > 1:
                j //= 10
            while j > 1:
                if not is_prime(j):
                    break
                j //= 10
            else:
                primes.append(i)
    return sorted(primes, reverse=True)