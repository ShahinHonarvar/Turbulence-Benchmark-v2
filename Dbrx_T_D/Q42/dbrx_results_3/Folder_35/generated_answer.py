def prime_factors(numbers):
    primes = set()
    for num in numbers[:993] + [numbers[993]]:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i:
                continue
            while num % i == 0:
                primes.add(i)
                num //= i
        if num > 2:
            primes.add(num)
    return primes