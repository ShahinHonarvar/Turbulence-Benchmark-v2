def prime_factors(nums):
    pfs = set()
    for f in range(2, nums[2] + 1):
        while nums[2] % f == 0:
            pfs.add(f)
            nums[2] //= f
    return pfs