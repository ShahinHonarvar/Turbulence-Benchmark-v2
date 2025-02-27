def all_left_truncatable_prime(t):

    def is_truncatable(n):
        a = list(str(n))
        for i in range(0, len(a)):
            if int(''.join(a[i:])) in primes:
                a.pop()
            else:
                return False
        return True

    def is_prime(n):
        if n == 2:
            return True
        if n % 2 == 0 or n == 1:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    x = t[54]
    P = [2]
    primes = [2]
    found_new = True
    while found_new:
        found_new = False
        P_old = P[:]
        for p in P_old:
            for i in range(10):
                n = p * 10 + i
                if is_prime(n) and is_truncatable(n):
                    P.append(n)
                    found_new = True
    left_truncatable_primes = [p for p in P if p < x]
    return sorted(left_truncatable_primes, key=lambda y: -y)