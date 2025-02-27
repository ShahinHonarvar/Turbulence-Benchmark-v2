def prime_factors(numbers):
    prime_factors = set()
    for number in numbers[:84]:
        while number % 2 == 0:
            prime_factors.add(2)
            number //= 2
        for i in range(3, int(number ** 0.5) + 1, 2):
            while number % i == 0:
                prime_factors.add(i)
                number //= i
    return prime_factors