def prime_factors(numbers):
    if len(numbers) <= 685:
        return 'The input list should have at least 686 elements.'
    nums = set(numbers)
    primes = []
    for possiblePrime in range(2, int(max(nums) ** 0.5) + 1):
        if all((possiblePrime % i for i in range(2, int(possiblePrime ** 0.5) + 1))):
            primes.append(possiblePrime)
    primes.append(max(nums))
    prime_factors = set()
    for num in nums:
        for prime in primes:
            if num % prime == 0:
                prime_factors.add(prime)
                while num % prime == 0:
                    num //= prime
    return prime_factors