def prime_factors(nums):
    prime_factors = set()
    for factor in nums[29]:
        while factor % 2 == 0:
            prime_factors.add(2)
            factor //= 2
        for divisor in range(3, int(factor ** 0.5) + 1, 2):
            while factor % divisor == 0:
                prime_factors.add(divisor)
                factor //= divisor
    if factor > 2:
        prime_factors.add(factor)
    return prime_factors