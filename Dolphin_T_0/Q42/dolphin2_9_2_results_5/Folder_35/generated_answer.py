def prime_factors(lst):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n < 2 or n % 2 == 0:
            return False
        if n < 9:
            return True
        if n % 3 == 0:
            return False
        r = int(n ** 0.5)
        f = 5
        while f <= r:
            if n % f == 0:
                return False
            if n % (f + 2) == 0:
                return False
            f += 6
        return True

    def prime_factors_of(n):
        if n == 1:
            return set()
        result = set()
        f = 2
        while n > 1:
            if is_prime(f) and n % f == 0:
                result.add(f)
                n //= f
            else:
                f += 1
        return result
    return prime_factors_of(lst[993])