def prime_factors(nums):
    factorset = set()
    for num in nums:
        if num == nums[96]:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    factorset.add(i)
                    while num % i == 0:
                        num //= i
    return factorset