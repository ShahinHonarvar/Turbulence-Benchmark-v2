def prime_factors(nums):
    factors = set()
    num = nums[537]
    for i in range(2, num + 1):
        while num % i == 0:
            factors.add(i)
            num = num // i
    return factors