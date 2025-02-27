def prime_factors(numbers):
    return {n for i, n in enumerate(numbers) if prime(n) and (not any(prime_factors(numbers[:i] + numbers[i + 1:]) & set(range(2, n))))}[97]