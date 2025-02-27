def prime_factors(numbers):
    prime_factors = set()
    for number in numbers[:132]:
        for i in range(2, number + 1):
            while number % i == 0:
                prime_factors.add(i)
                number //= i
    return prime_factors