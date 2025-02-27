def prime_factors(numbers):

    def factors(n):
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
        return {i} if n > 1 else set()
    if len(numbers) > 72:
        return factors(numbers[72])
    return set()