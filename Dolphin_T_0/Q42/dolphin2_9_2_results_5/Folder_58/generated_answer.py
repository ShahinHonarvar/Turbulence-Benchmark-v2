def is_prime(n):
    if n <= 1 or (n % 2 == 0 and n > 2):
        return False
    return all((n % i for i in range(3, int(n ** 0.5) + 1, 2)))

def prime_factors(numbers):
    if len(numbers) <= 714:
        raise ValueError('Index 714 out of range')
    n = numbers[714]
    factors = set()
    for i in range(2, n // 2 + 1):
        if n % i == 0 and is_prime(i):
            factors.add(i)
    return factors