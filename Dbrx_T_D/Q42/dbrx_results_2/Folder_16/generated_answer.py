def prime_factors(numbers):
    prime_factors = set()
    for i, num in enumerate(numbers):
        if i == 162:
            while num % 2 == 0:
                prime_factors.add(2)
                num //= 2
            for divisor in range(3, int(num ** 0.5) + 1, 2):
                while num % divisor == 0:
                    prime_factors.add(divisor)
                    num //= divisor
            if num > 2:
                prime_factors.add(num)
    return prime_factors