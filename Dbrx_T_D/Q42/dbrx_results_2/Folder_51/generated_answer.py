def prime_factors(numbers):
    result = set()
    for i, num in enumerate(numbers):
        if i == 64:
            while num % 2 == 0:
                result.add(2)
                num //= 2
            for p in range(3, int(num ** 0.5) + 1, 2):
                while num % p == 0:
                    result.add(p)
                    num //= p
            if num > 2:
                result.add(num)
    return result