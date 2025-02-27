def all_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    x = t[67]
    primes = {}
    for i in range(10 ** (x - 1) + 1, 10 ** x):
        if is_prime(i):
            primes[i] = i
        if is_right_truncatable(i):
            index = 1
            while index < i:
                i //= 10
                index *= 10
                if i > 1 and i not in primes:
                    if is_prime(i):
                        primes[i] = i
                else:
                    break
    return list(primes.keys())[::-1]