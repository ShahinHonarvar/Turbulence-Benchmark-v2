def prime_factors(numbers):

    def factors(n):
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
        return set([i]) if n > 1 else set()
    return factors(numbers[84])