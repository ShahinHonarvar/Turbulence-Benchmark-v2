def prime_factors(l):

    def ispr(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return {i for i in range(2, l[13] + 1) if l[13] % i == 0 and ispr(i)}