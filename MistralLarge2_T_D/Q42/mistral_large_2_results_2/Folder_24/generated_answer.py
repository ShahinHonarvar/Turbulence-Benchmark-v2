def prime_factors(numbers):

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
        d = 2
        while n > 1:
            while n % d == 0:
                if is_prime(d):
                    factors_set.add(d)
                n //= d
            d += 1
            if d * d > n:
                if n > 1:
                    factors_set.add(n)
                break
        return factors_set
    if len(numbers) > 74:
        return factors(numbers[74])
    else:
        return set()