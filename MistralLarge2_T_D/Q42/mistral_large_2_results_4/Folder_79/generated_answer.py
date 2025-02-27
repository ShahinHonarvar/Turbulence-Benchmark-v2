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
        factors_set = set()
        divisor = 2
        while n >= 2:
            if n % divisor == 0:
                if is_prime(divisor):
                    factors_set.add(divisor)
                n //= divisor
            else:
                divisor += 1
        return factors_set
    if len(lst) > 63:
        return factors(lst[63])
    return set()