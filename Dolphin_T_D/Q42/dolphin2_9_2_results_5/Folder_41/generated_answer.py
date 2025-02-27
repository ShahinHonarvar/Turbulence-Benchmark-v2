def prime_factors(numb_list):

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

    def prime_factors_of_numb(n):
        factors = set()
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            elif is_prime(i):
                factors.add(i)
                n //= i
            else:
                i += 1
        if n > 1:
            factors.add(n)
        return factors
    return prime_factors_of_numb(numb_list[84])