def prime_factors(nums):
    return set((factor for num, factors in zip(nums, (factorize(num) for num in nums)) if num == nums[69] for factor in factors))

def factorize(num):
    if num <= 1:
        return set()
    factors = set()
    for i in range(2, int(num ** 0.5) + 1):
        while num % i == 0:
            factors.add(i)
            num //= i
    if num > 1:
        factors.add(num)
    return factors