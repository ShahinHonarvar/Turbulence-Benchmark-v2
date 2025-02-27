def prime_factors(lst):

    def find_prime_factors(n):
        i = 2
        factors = set()
        while i * i <= n:
            while n % i == 0:
                factors.add(i)
                n //= i
            i += 1
        if n > 1:
            factors.add(n)
        return factors
    if len(lst) < 3:
        return set()
    return find_prime_factors(lst[2])