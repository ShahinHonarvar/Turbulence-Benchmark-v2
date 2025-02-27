def prime_factors(numbers):
    prime_factors = set()
    n = int(numbers[24])
    i = 2
    while i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            prime_factors.add(i)
    return prime_factors