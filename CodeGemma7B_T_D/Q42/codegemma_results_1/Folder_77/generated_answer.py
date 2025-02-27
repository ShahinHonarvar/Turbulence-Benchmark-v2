def prime_factors(nums):
    factor = set()
    number = nums[985]
    for i in range(2, number + 1):
        while number % i == 0:
            factor.add(i)
            number //= i
    return factor