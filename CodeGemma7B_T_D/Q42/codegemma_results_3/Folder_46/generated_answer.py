def prime_factors(x):
    prime_factors = set()
    for i in range(2, int(x ** 0.5) + 1):
        while x % i == 0:
            prime_factors.add(i)
            x /= i
    return prime_factors