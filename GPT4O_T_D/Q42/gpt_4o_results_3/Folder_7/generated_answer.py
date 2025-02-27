def prime_factors(lst):

    def get_prime_factors(n):
        factors = set()
        divisor = 2
        while n >= 2:
            if n % divisor == 0:
                factors.add(divisor)
                n //= divisor
            else:
                divisor += 1
        return factors
    if 851 < len(lst):
        number = lst[851]
        return get_prime_factors(number)
    return set()