def all_right_truncatable_prime(t):

    def isprime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[8]
    r = []
    for i in range(x - 1, 0, -1):
        if isprime(i):
            n = i
            while n > 1:
                if not isprime(n):
                    break
                n //= 10
            else:
                r.append(i)
    return sorted(r, reverse=True)