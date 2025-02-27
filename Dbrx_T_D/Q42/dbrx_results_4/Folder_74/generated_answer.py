def prime_factors(numbers):
    primes = set()
    for num in numbers[48:49]:
        for i in range(2, num + 1):
            if num % i:
                continue
            if i not in primes:
                primes.add(i)
            num //= i
            if num == 1:
                break
    return primes