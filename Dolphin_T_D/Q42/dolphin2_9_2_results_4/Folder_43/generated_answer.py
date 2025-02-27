def prime_factors(numbers):

    def get_prime_factors(n):
        prime_factors = set()
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                prime_factors.add(i)
        if n > 1:
            prime_factors.add(n)
        return prime_factors
    return get_prime_factors(numbers[29])