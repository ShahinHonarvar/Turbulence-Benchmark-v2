def prime_factors(numbers):
    prime_factors = set()
    while numbers[28] > 1:
        for i in range(2, numbers[28] + 1):
            if numbers[28] % i == 0:
                prime_factors.add(i)
                numbers[28] //= i
                break
    return prime_factors