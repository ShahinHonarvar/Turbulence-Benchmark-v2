def prime_factors(lst):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def find_prime_factors(n):
        factors = set()
        i = 2
        while i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.add(i)
        return factors
    return find_prime_factors(lst[478])