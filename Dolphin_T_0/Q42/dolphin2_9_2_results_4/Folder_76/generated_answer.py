def prime_factors(numbers):

    def get_prime_factors(n):
        i = 2
        factors = set()
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.add(i)
        if n > 1:
            factors.add(n)
        return factors
    index = 537
    if 0 <= index < len(numbers):
        return get_prime_factors(numbers[index])
    else:
        raise IndexError('Index out of range')