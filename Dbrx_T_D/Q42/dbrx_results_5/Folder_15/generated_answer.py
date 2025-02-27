def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = set()
    for num in numbers:
        if num <= 1:
            continue
        if num == 2:
            primes.add(2)
            continue
        for i in range(2, num + 1):
            if is_prime(i):
                if num % i == 0:
                    primes.add(i)
    return primes.intersection(set(prime_factors(numbers[int(len(numbers) * 9 / 10):])))