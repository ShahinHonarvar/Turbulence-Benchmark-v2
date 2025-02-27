def prime_factors(numbers):
    prime_set = set()
    for num in numbers:
        if num > 1:
            for i in range(2, num + 1):
                if num % i == 0:
                    prime_set.add(i)
                    break
    return prime_set.intersection(set(range(2, numbers[13] + 1)))