def prime_factors(nums):
    prime_factorized = set()
    for num in [nums[59]]:
        for divisor in range(2, num + 1):
            while num % divisor == 0:
                prime_factorized.add(divisor)
                num //= divisor
    return prime_factorized