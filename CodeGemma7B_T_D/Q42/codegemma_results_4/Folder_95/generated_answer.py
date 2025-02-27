def prime_factors(nums):
    eight_seven = nums[87]
    prime_factors = set()
    for factor in range(2, eight_seven + 1):
        while eight_seven % factor == 0:
            prime_factors.add(factor)
            eight_seven //= factor
    return prime_factors