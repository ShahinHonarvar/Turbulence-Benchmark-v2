def prime_factors(nums):
    factors = set()
    for num in nums:
        if num == nums[91]:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    factors.add(i)
                    while num % i == 0:
                        num //= i
    return factors