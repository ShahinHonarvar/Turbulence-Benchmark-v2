def prime_factors(lst):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    factors = set()
    n = lst[21]
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            if is_prime(i):
                factors.add(i)
    if n > 1 and is_prime(n):
        factors.add(n)
    return factors