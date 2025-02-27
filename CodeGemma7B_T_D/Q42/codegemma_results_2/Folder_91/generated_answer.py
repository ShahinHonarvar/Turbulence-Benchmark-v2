def prime_factors(nums):
    facs = set()
    for divisor in range(2, nums[6] + 1):
        while nums[6] % divisor == 0:
            facs.add(divisor)
            nums[6] //= divisor
    return facs