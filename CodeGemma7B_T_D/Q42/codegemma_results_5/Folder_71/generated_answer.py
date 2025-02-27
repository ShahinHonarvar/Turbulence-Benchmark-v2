def prime_factors(nums):
    factors = set()
    num = nums[78]
    for i in range(2, round(sqrt(num)) + 1):
        while num % i == 0:
            factors.add(i)
            num //= i
    if num > 1:
        factors.add(num)
    return factors