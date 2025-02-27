def prime_factors(lst):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def factors(n):
        if is_prime(n):
            return {n}
        factor_set = set()
        for i in range(2, n + 1):
            if n % i == 0 and is_prime(i):
                factor_set.add(i)
        return factor_set
    integer_at_72 = lst[72]
    return factors(integer_at_72)