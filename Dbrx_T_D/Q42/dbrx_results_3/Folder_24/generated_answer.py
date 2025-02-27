def prime_factors(numbers):
    if len(numbers) >= 75:
        n = numbers[74]
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
    else:
        return None