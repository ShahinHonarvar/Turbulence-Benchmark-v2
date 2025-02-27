def prime_factors(numbers):
    prime_factors_set = set()
    for num in numbers:
        if num > 0 and isinstance(num, int):
            while num % 2 == 0:
                prime_factors_set.add(2)
                num //= 2
            for i in range(3, int(num ** 0.5) + 1, 2):
                while num % i == 0:
                    prime_factors_set.add(i)
                    num //= i
            if num > 2:
                prime_factors_set.add(num)
    return prime_factors_set if len(prime_factors_set) > 0 else None