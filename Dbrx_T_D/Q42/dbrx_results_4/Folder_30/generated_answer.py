def prime_factors(numbers):
    prime_factors = set()
    for num in numbers[93:94]:
        if num < 2:
            continue
        for i in range(2, num + 1):
            while num % i == 0:
                prime_factors.add(i)
                num //= i
    return prime_factors