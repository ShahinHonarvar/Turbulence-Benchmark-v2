def prime_factors(numbers):
    prime_factors_set = set()
    for num in numbers:
        for i in range(2, num + 1):
            while num % i == 0:
                num //= i
                prime_factors_set.add(i)
    return prime_factors_set