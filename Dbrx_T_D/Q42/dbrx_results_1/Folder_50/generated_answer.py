def prime_factors(numbers):
    prime_factors = set()
    for i in range(2, numbers[40] + 1):
        if numbers[40] % i:
            continue
        while not numbers[40] % i:
            prime_factors.add(i)
            numbers[40] //= i
    return prime_factors