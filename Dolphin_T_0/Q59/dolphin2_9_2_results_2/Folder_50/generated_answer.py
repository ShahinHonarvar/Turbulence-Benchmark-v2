def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[57]
    primes = []
    for n in range(x - 1, 1, -1):
        if '0' in str(n):
            continue
        while n > 1:
            if not is_prime(n):
                break
            n = int(str(n)[1:])
        else:
            primes.append(n)
    return sorted(primes, reverse=True)