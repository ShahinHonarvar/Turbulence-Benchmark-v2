def prime_factors(numbers):
    prime_factors = set()
    for num in numbers[:54]:
        for i in range(2, num + 1):
            if num % i == 0:
                prime_factors.add(i)
                num //= i
                if num == 1:
                    break
    return prime_factors