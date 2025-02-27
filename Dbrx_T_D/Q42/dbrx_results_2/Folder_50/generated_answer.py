def prime_factors(numbers):
    prime_factors = set()
    for num in numbers[:41]:
        for i in range(2, num + 1):
            if num % i == 0:
                prime_factors.add(i)
    return prime_factors