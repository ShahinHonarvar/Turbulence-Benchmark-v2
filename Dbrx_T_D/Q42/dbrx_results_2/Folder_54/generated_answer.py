def prime_factors(numbers):
    prime_factors = set()
    num = numbers[51]
    for i in range(2, num + 1):
        while num % i == 0:
            prime_factors.add(i)
            num //= i
    return prime_factors