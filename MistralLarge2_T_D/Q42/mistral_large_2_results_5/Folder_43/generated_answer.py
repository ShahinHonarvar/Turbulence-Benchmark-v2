def prime_factors(int_list):

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
        factors_set = set()
        i = 2
        while i * i <= n:
            while n % i == 0:
                factors_set.add(i)
                n //= i
            i += 1
        if n > 1:
            factors_set.add(n)
        return factors_set
    if len(int_list) > 29:
        return factors(int_list[29])
    return set()