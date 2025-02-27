def prime_factors(nums):
    factors = set()
    num = nums[702]
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            factors.add(i)
    if num != 1:
        factors.add(num)
    return factors