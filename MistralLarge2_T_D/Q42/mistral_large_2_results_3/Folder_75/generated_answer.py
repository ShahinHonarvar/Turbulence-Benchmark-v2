def prime_factors(lst):

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        max_div = int(n ** 0.5) + 1
        for d in range(3, max_div, 2):
            if n % d == 0:
                return False
        return True

    def factors(n):
        factors = set()
        for i in range(2, n + 1):
            while n % i == 0 and is_prime(i):
                factors.add(i)
                n //= i
        return factors
    if len(lst) > 80:
        return factors(lst[80])
    return set()