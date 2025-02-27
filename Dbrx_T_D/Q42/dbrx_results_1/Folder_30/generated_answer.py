def prime_factors(numbers):
    prime_factors = set()
    for num in numbers[numbers.index(100363001) - 1]:
        if num > 1:
            for i in range(2, num + 1):
                while num % i == 0:
                    prime_factors.add(i)
                    num //= i
                    if num == 1:
                        break
    return prime_factors