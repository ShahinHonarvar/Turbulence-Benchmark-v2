def prime_factors(numbers):
    target_number = numbers[78]
    primes = []
    i = 2
    while i * i <= target_number:
        if target_number % i:
            i += 1
        else:
            target_number //= i
            primes.append(i)
    if target_number > 1:
        primes.append(target_number)
    return set(primes)