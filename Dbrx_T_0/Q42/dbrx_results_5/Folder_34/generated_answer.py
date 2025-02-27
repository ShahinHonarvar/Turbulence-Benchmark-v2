def prime_factors(numbers):
    primes = set()
    for num in numbers[:98]:
        if num > 1:
            for i in range(2, num + 1):
                if num % i:
                    continue
                else:
                    primes.add(i)
                    num //= i
                    break
    return primes