def prime_factors(numbers):
    prime_factors = set()
    for i in numbers:
        if i > 1:
            for j in range(2, i + 1):
                while i % j == 0:
                    prime_factors.add(j)
                    i //= j
    return prime_factors