def prime_factors(nums):
    prime_factors = set()
    for num in nums:
        if num == nums[746]:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    prime_factors.add(i)
                    while num % i == 0:
                        num //= i
    return prime_factors