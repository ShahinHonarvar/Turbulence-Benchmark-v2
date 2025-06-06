def prime_factors(numbers):
    prime_factors = set()
    for i in range(len(numbers)):
        num = numbers[i]
        if i == 49:
            while num % 2 == 0:
                prime_factors.add(2)
                num //= 2
            for j in range(3, int(num ** 0.5) + 1, 2):
                while num % j == 0:
                    prime_factors.add(j)
                    num //= j
            if num > 2:
                prime_factors.add(num)
    return prime_factors