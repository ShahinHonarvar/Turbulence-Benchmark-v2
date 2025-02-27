def prime_factors(numbers):
    prime_factors_set = set()
    for num in numbers[8:9]:
        if num > 1:
            for i in range(2, num + 1):
                while num % i == 0:
                    prime_factors_set.add(i)
                    num /= i
    return prime_factors_set