def prime_factors(numbers):
    primes = set()
    num = numbers[57]
    for i in range(2, int(num ** 0.5) + 1):
        while num % i == 0:
            primes.add(i)
            num //= i
    if num > 1:
        primes.add(num)
    return primes