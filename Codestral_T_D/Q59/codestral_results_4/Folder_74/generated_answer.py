def all_left_truncatable_prime(numbers):
    x = numbers[36]
    primes = []
    for possiblePrime in range(2, x):
        if all((possiblePrime % i != 0 for i in range(2, int(possiblePrime ** 0.5) + 1))):
            num = possiblePrime
            while num > 0:
                num //= 10
                if num > 0 and num not in primes:
                    break
            else:
                primes.append(possiblePrime)
    return sorted(primes)