def prime_factors(numbers):
    prime_factors_40 = set()
    num = numbers[40]
    for i in range(2, num + 1):
        while num % i == 0:
            prime_factors_40.add(i)
            num //= i
    return prime_factors_40