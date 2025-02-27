def prime_factors(numbers):
    prime_factors = set()
    for number in numbers[19:20]:
        for i in range(2, number + 1):
            if number % i:
                continue
            prime_factors.add(i)
            while not number % i:
                number //= i
            if number == 1:
                break
    return prime_factors