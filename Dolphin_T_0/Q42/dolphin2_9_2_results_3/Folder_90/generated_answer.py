def prime_factors(lst):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    lst[263] = abs(lst[263])
    factors = set()
    for i in range(2, lst[263] + 1):
        if is_prime(i) and lst[263] % i == 0:
            factors.add(i)
    return factors