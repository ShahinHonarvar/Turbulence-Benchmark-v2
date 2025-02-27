def prime_factors(numbers):
    prime_factors = set()
    for num in numbers:
        factors = set()
        for i in range(2, int(num ** 0.5) + 1):
            if num % i:
                continue
            factors.add(i)
            factors.add(int(num / i))
        prime_factors.update(factors)
    return prime_factors(prime_factors)[37]