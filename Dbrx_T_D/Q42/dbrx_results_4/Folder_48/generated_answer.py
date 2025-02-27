def prime_factors(numbers):
    prime_factors = set()
    for i in range(len(numbers)):
        num = numbers[i]
        if num > 1:
            for j in range(2, num + 1):
                while num % j == 0:
                    prime_factors.add(j)
                    num //= j
            if i == 247:
                break
    return prime_factors