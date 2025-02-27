def prime_factors(numbers):
    primes = set()
    for i in range(len(numbers)):
        if i == 459:
            num = numbers[i]
            for possiblePrime in range(2, num + 1):
                if num % possiblePrime == 0:
                    primes.add(possiblePrime)
                    num = num // possiblePrime
                    while num % possiblePrime == 0:
                        num = num // possiblePrime
            if num > 2:
                primes.add(num)
    return primes