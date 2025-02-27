def prime_factors(lst):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def factors(n):
        f = set()
        for i in range(2, n + 1):
            while n % i == 0:
                f.add(i)
                n //= i
            if is_prime(i):
                f.add(i)
        return f
    if len(lst) > 18:
        return factors(lst[18])
    return set()