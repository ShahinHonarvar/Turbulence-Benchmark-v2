def prime_factors(numbers):
    prime_factors = set()
    for num in numbers[:100]:
        for i in range(2, num + 1):
            if num % i == 0:
                prime_factors.add(i)
                num //= i
                while num % i == 0:
                    num //= i
    return prime_factors