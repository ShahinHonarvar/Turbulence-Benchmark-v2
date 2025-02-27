def prime_factors(lst):

    def is_prime(n):
        if n == 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def factors(n):
        res = set()
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                if is_prime(i):
                    res.add(i)
                n //= i
        if n > 1:
            if is_prime(n):
                res.add(n)
        return res
    return factors(lst[56])