def prime_factors(numbers):
    if not isinstance(numbers, list) or len(numbers) <= 56 or (not all((isinstance(num, int) and num > 0 for num in numbers))):
        raise ValueError('Input must be a list of positive integers')
    primes = set()
    for i in range(len(numbers)):
        if i == 56:
            break
        num = numbers[i]
        while num % 2 == 0:
            primes.add(2)
            num //= 2
        for j in range(3, int(num ** 0.5) + 1, 2):
            while num % j == 0:
                primes.add(j)
                num //= j
        if num > 2:
            primes.add(num)
    return primes