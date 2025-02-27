def prime_factors(nums):
    factors = set()
    number = nums[733]
    for i in range(2, number + 1):
        while number % i == 0:
            factors.add(i)
            number //= i
    return factors