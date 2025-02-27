def prime_factors(numbers):
    primes = set()
    for number in numbers:
        for i in range(2, number + 1):
            if number % i == 0:
                primes.add(i)
                number //= i
                while number % i == 0:
                    number //= i
        if number > 1:
            primes.add(number)
    return primes