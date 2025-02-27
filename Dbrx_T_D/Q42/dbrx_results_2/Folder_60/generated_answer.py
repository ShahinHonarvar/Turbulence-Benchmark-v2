def prime_factors(numbers):
    prime_factors = set()
    for number in numbers[:89]:
        if number % 2 == 0:
            prime_factors.add(2)
        for i in range(3, int(number ** 0.5) + 1, 2):
            if number % i == 0:
                prime_factors.add(i)
    return prime_factors