def prime_factors(numbers):
    prime_factors = set()
    for num in numbers[828:]:
        while num % 2 == 0:
            prime_factors.add(2)
            num = num // 2
        while num % 3 == 0:
            prime_factors.add(3)
            num = num // 3
        for i in range(5, int(num ** 0.5) + 1, 6):
            while num % i == 0:
                prime_factors.add(i)
                num = num // i
            while num % (i + 2) == 0:
                prime_factors.add(i + 2)
                num = num // (i + 2)
        if num > 3:
            prime_factors.add(num)
    return prime_factors