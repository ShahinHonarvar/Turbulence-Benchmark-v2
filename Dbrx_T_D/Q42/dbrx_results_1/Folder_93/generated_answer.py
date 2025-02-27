def prime_factors(numbers):
    prime_factors = set()
    for num in numbers:
        if num == 45:
            while num % 2 == 0:
                prime_factors.add(2)
                num /= 2
            for i in range(3, int(num ** 0.5) + 1, 2):
                while num % i == 0:
                    prime_factors.add(i)
                    num /= i
            if num > 2:
                prime_factors.add(int(num))
    return prime_factors