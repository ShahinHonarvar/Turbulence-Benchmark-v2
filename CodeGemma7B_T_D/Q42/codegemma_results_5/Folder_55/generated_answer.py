def prime_factors(nums):
    prime_set = set()
    for num in nums:
        if num > 1:
            for divisor in range(2, int(num ** 0.5) + 1):
                if num % divisor == 0:
                    prime_set.add(divisor)
                    num //= divisor
    return prime_set