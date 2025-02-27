def prime_factors(nums):
    product = nums[100]
    factors = set()
    for i in range(2, int(product ** 0.5) + 1):
        while product % i == 0:
            product //= i
            factors.add(i)
    return factors