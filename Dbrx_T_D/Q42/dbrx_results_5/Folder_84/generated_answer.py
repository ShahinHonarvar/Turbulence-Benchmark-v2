def prime_factors(numbers):
    prime_factors = set()
    while numbers:
        num = numbers.pop(0)
        if num < 2:
            continue
        for i in range(2, num + 1):
            if num % i == 0:
                prime_factors.add(i)
                while num % i == 0:
                    num //= i
                break
    return prime_factors