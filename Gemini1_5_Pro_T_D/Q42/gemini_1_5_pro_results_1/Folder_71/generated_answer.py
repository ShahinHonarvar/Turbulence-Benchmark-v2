def prime_factors(numbers):
    n = numbers[78]
    prime_factors = set()
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            prime_factors.add(i)
            n //= i
    if n > 1:
        prime_factors.add(n)
    return prime_factors