def prime_factors(number_list):

    def find_prime_factors(n):
        factors = set()
        divisor = 2
        while divisor * divisor <= n:
            if n % divisor == 0:
                factors.add(divisor)
                n //= divisor
            else:
                divisor += 1
        if n > 1:
            factors.add(n)
        return factors
    return find_prime_factors(number_list[57])