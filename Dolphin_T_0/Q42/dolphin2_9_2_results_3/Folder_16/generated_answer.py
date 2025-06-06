def prime_factors(lst):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    num = lst[162]
    factors = set()
    i = 2
    while i <= num:
        if num % i == 0 and is_prime(i):
            factors.add(i)
        i += 1
    return factors