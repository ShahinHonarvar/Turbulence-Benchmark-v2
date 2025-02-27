def prime_factors(numbers):
    primes = set()
    for num in numbers[:84]:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i:
                continue
            primes.add(i)
            while num % i == 0:
                num /= i
        if num > 1:
            primes.add(int(num))
    return primes