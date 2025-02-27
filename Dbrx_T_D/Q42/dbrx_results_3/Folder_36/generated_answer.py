def prime_factors(numbers):
    prime_factors = set()
    for i in numbers:
        if i <= 1:
            continue
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                prime_factors.add(j)
                while i % j == 0:
                    i //= j
        if i > 1:
            prime_factors.add(i)
    if len(numbers) > 990:
        return prime_factors.intersection(set(numbers[990]))
    else:
        return None