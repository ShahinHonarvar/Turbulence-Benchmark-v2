def prime_factors(nums):
    factors = set()
    for num in nums:
        if num == nums[685]:
            for i in range(2, int(num ** 0.5) + 1):
                while num % i == 0:
                    factors.add(i)
                    num //= i
    return factors