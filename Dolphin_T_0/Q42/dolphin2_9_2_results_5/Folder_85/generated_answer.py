def prime_factors(numAH):

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
    num = numAH[23]
    factors = set()
    for i in range(2, num + 1):
        if num % i == 0 and is_prime(i):
            factors.add(i)
    return factors