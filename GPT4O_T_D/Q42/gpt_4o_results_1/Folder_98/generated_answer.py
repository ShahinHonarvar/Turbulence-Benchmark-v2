def prime_factors(nums):
    if len(nums) < 5:
        return set()
    num = nums[4]
    i = 2
    factors = set()
    while i * i <= num:
        while num % i == 0:
            factors.add(i)
            num //= i
        i += 1
    if num > 1:
        factors.add(num)
    return factors