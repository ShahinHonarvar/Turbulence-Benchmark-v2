def all_right_truncatable_prime(tup):
    x = tup[3]
    primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for i in range(x, 0, -1):
        if is_prime(i):
            j = i
            while j != 0:
                if j % 10 != 0 and (not is_prime(j // 10)):
                    break
                j //= 10
            else:
                primes.append(i)
    return sorted(primes, reverse=True)