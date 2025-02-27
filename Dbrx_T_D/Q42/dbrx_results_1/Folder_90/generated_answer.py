def prime_factors(numbers):
    prime_factors = set()
    num = numbers[263]
    for i in range(2, num + 1):
        if num % i:
            continue
        prime_factors.add(i)
        while num % i == 0:
            num /= i
    return prime_factors