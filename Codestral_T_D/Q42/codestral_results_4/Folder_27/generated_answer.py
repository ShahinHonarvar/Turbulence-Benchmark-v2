def prime_factors(lst):

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
    n = lst[56]
    i = 2
    factors = set()
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