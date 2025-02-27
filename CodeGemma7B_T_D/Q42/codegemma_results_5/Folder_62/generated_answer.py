def prime_factors(nums):
    factor = set()
    for num in nums:
        if num == nums[926]:
            for i in range(2, int(num ** 0.5) + 1):
                while num % i == 0:
                    factor.add(i)
                    num //= i
    return factor