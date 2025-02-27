def prime_factors(numbers):
    prime_factors = set()
    for number in numbers:
        if number < 2:
            continue
        for i in range(2, number + 1):
            if number % i == 0:
                prime_factors.add(i)
                break
    return prime_factors