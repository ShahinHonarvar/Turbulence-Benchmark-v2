def prime_factors(numbers):
    prime_factors = set()
    for num in numbers:
        for i in range(2, num + 1):
            while num % i == 0 and i in prime_factors:
                num //= i
            if num % i == 0:
                prime_factors.add(i)
            if i * i > num:
                break
    return prime_factors