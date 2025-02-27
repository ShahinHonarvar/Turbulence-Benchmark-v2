def prime_factors(numbers):
    if len(numbers) <= 790:
        return 'Error: List is too short, must be at least index 790'
    else:
        n = numbers[790]
        i = 2
        primes = set()
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                primes.add(i)
        if n > 1:
            primes.add(n)
        return primes